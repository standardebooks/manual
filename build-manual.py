#!/usr/bin/env python3
"""
This executable builds takes RST files comprising the SE manual and outputs final PHP files for publication to the SE website.
"""

import os
import argparse
from html import escape
from pathlib import Path
import subprocess
import sys
import tempfile
from bs4 import BeautifulSoup, NavigableString, Tag
from natsort import natsorted
import regex

BLOCK_LEVEL_ELEMENTS = ["p", "figure", "ol", "ul", "section", "pre", "blockquote", "table"]

RST_ROLES = """.. role:: html(code)
	:language: html
.. role:: css(code)
	:language: css
.. role:: bash(code)
	:language: bash
.. role:: path(code)
.. role:: italics(emphasis)
	:class: i
.. role:: ws(code)
	:class: ws
.. role:: utf(code)
	:class: utf
.. role:: value(code)
	:class: value
.. role:: string(code)
	:class: string

"""

RST_ROLES_LINE_COUNT = len(RST_ROLES.splitlines())

def process_ids(section: Tag, current_id: str, current_number: int) -> int:
	"""
	Generate potentially nested numeric IDs for a manual directive.
	"""

	for elem in section.children:
		if isinstance(elem, Tag):
			# By convention, if there's a "no-numbering" class then skip the section
			if elem.has_attr("class") and elem["class"] != "no-numbering":
				continue

			if elem.name == "section" or (elem.name == "li" and elem.parent.name == "ol"):
				new_id = f"{current_id}.{current_number}"
				elem["id"] = new_id
				process_ids(elem, new_id, 1)
				current_number = current_number + 1

			# Descend into <ol>s, and save the current number we get back so that we don't reset it if we
			# next move on to further sibling sections
			if elem.name == "ol":
				current_number = process_ids(elem, current_id, current_number)

	return current_number

class TocItem:
	"""
	An item in the manual table of contents.
	"""

	def __init__(self, number: str, title: str, filename: str):
		self.number = number
		self.title = title
		self.filename = filename
		self.items = []

def make_one_page(dest_directory):
	"""
	Generate one-page php file of the manual.
	"""
	# Get all php files in destination directory.
	php_files = list(filter(lambda x: x.endswith("php"), os.listdir(dest_directory)))
	index = php_files.pop(php_files.index("index.php"))

	with open(dest_directory + "/" + index, "r", encoding="utf-8") as f:
		index_soup = BeautifulSoup(f, features="html.parser")
		php_tags = regex.findall(r"<\?.+?\?>", index_soup.prettify(formatter=None), regex.S)

	# The frontmatter contains all needed tags and texts at the beginning of the one-page manual
	index_soup.find("section")["id"] = "0"
	frontmatter = index_soup.find("section")
	# Remove short form ToC
	frontmatter.find_all("section")[-1].decompose()

	# Get ToC
	with open(dest_directory + "/" + php_files[0], "r", encoding="utf-8") as f:
		toc = str(BeautifulSoup(f, features="html.parser").find("nav"))

	# Format hrefs in ToC for onepager
	toc = regex.sub(r"(?<=href\=\")([/a-z0-9\.-]+?)(?=#)", "", toc)
	toc = regex.sub(r"(?<=href\=\")(?P<href>[/0-9a-z-\.]+(?<=/)(?P<chapter>\d+)(?=-)[/0-9a-z-\.]+(?=\"))", r"#\g<chapter>", toc)
	toc = regex.sub(r"(?<=href=\")(/manual.+?\d)(?=\")", r"#0", toc)

	# Get chapter tags/text without toc
	bodymatter = []
	php_files = list(filter(lambda x: regex.match(r"^\d.+", x), php_files))

	for file in php_files:
		with open(dest_directory + "/" + file, "r", encoding="utf-8") as f:
			soup = BeautifulSoup(f, features="html.parser")

		bodymatter.append(soup.find_all("section")[0])

	# Writing the one page manual php file (overwrites if exist)
	onepage = dest_directory + "/single-page.php"
	with open(onepage, "w+", encoding="utf-8") as f:
		# Rewind file to erase old file if exist
		f.seek(0)

		# Write php tags and ToC
		f.write(php_tags[0] + php_tags[1] + "\n")
		f.write('\t<main class="manual">\n')
		f.write("\t\t" + php_tags[2] + "\n")
		f.write("\t\t\n")
		f.write(toc + "\n")

		# Write frontmatter
		f.write("<article>\n")
		f.write(str(frontmatter) + "\n")
		f.write("</article>\n")

		# Write bodymatter
		for chapter in bodymatter:
			f.write("<article>\n")
			f.write(str(chapter) + "\n")
			f.write("</article>\n")

		# Close with tags and final php tag
		f.write("</main>\n")
		f.write(php_tags[3])
		f.truncate()


def main() -> int:
	"""
	Entry point for the executable.
	"""

	parser = argparse.ArgumentParser(description="Build the Standard Ebooks Manual of Style from a set of .rst files.")
	parser.add_argument("source_directory", metavar="SOURCE_DIRECTORY", help="a directory containing .rst files comprising the Standard Ebooks Manual of Style")
	parser.add_argument("dest_directory", metavar="DEST_DIRECTORY", help="a directory to place the output .php files")
	args = parser.parse_args()

	return_code = 0

	if not os.path.isdir(args.source_directory):
		print(f"Not a directory: `{args.source_directory}`")
		return 1

	if not os.path.isdir(args.dest_directory):
		print(f"Not a directory: `{args.dest_directory}`")
		return 1

	toc = []

	header_path = Path(args.source_directory) / "templates" / "header.html"
	footer_path = Path(args.source_directory) / "templates" / "footer.html"

	try:
		with open(header_path, "r", encoding="utf-8") as file:
			header_html = file.read()
	except:
		print(f"Couldn’t open `{header_path}`")
		return 1

	try:
		with open(footer_path, "r", encoding="utf-8") as file:
			footer_html = file.read()
	except:
		print(f"Couldn’t open `{footer_path}`")
		return 1

	with tempfile.TemporaryDirectory() as work_directory:
		for filename in os.listdir(args.source_directory):
			if not filename.endswith(".rst"):
				continue

			with open(Path(args.source_directory) / filename, "r", encoding="utf-8") as file:
				rst = file.read()

			# Add our special RST roles to the top of the file before processing
			rst = RST_ROLES + rst

			result = subprocess.run(["rst2html5"], input=rst.encode(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)

			errors = result.stderr.decode().strip()
			if errors:
				print(filename)
				# Because we add the RST roles to the top of the file, we have to subtract those lines to get the
				# *real* line number in the RST file that the error occurs in.
				errors = regex.sub("<stdin>:([0-9]+)", lambda exp: "\tLine {}".format(int(exp.groups()[0]) - RST_ROLES_LINE_COUNT), errors).rstrip()
				print(errors)
				return_code = 1

			html = result.stdout.decode().strip()

			matches = regex.findall(r"<h1>(.+?)</h1>", html)
			if matches:
				title = matches[0]

			# Remove empty spans
			html = regex.sub(r"<span>[^>]*?</span>", "", html, flags=regex.DOTALL)

			# SE extension: :italics:`abc <def>` will generate a link like so: <i><a href="def">abc</a></i>
			html = regex.sub(r"<em class=\"i\">([^>]+?) &lt;([^<]+?)&gt;</em>", r"""<i><a href="\2">\1</a></i>""", html)

			# SE extension: change <em class="i"> to <i>
			html = regex.sub(r"<em class=\"i\">([^<]+?)</em>", r"<i>\1</i>", html)

			# Change :ws: and :utf: markers to <span>s
			html = regex.sub(r":(ws|utf):`([^`]+?)`", r"""<span class="\1">\2</span>""", html)

			# Remove comments
			html = regex.sub(r"<!--.+?-->", "", html)

			# Pygments doesn't add colors to html that is just a namespaced attribute, like :html:`xml:lang`. Add that here.
			html = regex.sub(r"""<code class="html">([a-zA-Z\-:]+?)</code>""", r"""<code class="html"><span class="na">\1</span></code>""", html)

			root_number = None
			matches = regex.findall(r"^([0-9]+)\-", filename)
			if matches:
				root_number = matches[0]

			# Now we have some cleaned up HTML.
			# Start parsing the various <section> and <ol> elements to number them.
			soup = BeautifulSoup(html, "html.parser")

			if root_number:
				# Set the ID on the top-level manual section
				top_level_section = soup.select("body > section")[0]

				top_level_section["id"] = root_number

				# Do the actual numbering
				process_ids(top_level_section, root_number, 1)

				# Record the number and its h2 children in the ToC
				toc_item = TocItem(root_number, title, filename.replace(".rst", ""))
				for header in soup.select("h2"):
					toc_item.items.append(TocItem(header.parent["id"], header.text, None))

				toc.append(toc_item)

			# rst2html5 doesn't wrap the first child of <li> elements in <p>.
			# Try to do that here.
			for li_item in soup.select("li"):
				need_wrapping = []
				for elem in li_item.contents:
					if isinstance(elem, NavigableString) or elem.name not in BLOCK_LEVEL_ELEMENTS:
						need_wrapping.append(elem)

					if elem.name in BLOCK_LEVEL_ELEMENTS:
						break

				if need_wrapping:
					new_tag = soup.new_tag("p")

					for elem in need_wrapping:
						new_tag.append(elem)

					li_item.insert(0, new_tag)

			# Now that we've got our structure done, insert <aside>s that have the section numbers in them.
			for elem in soup.find_all("", attrs={"id": regex.compile(r"^[0-9\.]+$")}):
				aside = soup.new_tag("aside")
				aside["class"] = "number"

				# Add a link to the section within the section <aside>, but only if it is not the main section number (like "2" or "8")
				if regex.match(r"^[0-9]$", elem["id"]):
					aside.string = elem["id"]
				else:
					link = soup.new_tag("a")
					link["href"] = f"#{elem['id']}"
					link.string = elem["id"]
					aside.insert(0, link)

				elem.insert(0, aside)

			html = str(soup)

			# Now that we've added IDs and <aside>s, remove the now-unnecessary "no-numbering" class
			html = html.replace(" class=\"no-numbering\"", "")

			# Add a <b> around the first word in a bash command, to highlight it.
			html = regex.sub(r"<code class=\"bash\">([a-z]+) ", r"""<code class="bash"><b>\1</b> """, html)

			# Add syntax highlighting around value strings
			html = regex.sub(r"<code class=\"value\">([^<]+?)</code>", r"""<code class="bash"><span class="s">\1</span></code>""", html)

			# Remove everything up to and including the body element so that we can add our own headers and footers
			html = regex.sub(r".+?<body>", "", html, flags=regex.DOTALL)
			html = regex.sub(r"</body>.*", "", html, flags=regex.DOTALL)

			# If we use CSS properties like -epub-hyphens, the colorizer considers them errors and adds error coloring. Remove that here.
			html = regex.sub(r"""<span class="err">-</span><span class="n">(.+?)</span>""", r"""<span class="k">-\1</span>""", html)

			# Convert spaces to tabs
			html = regex.sub(r"    ", "\t", html)

			# Add PHP headers and footers
			html = header_html + html + footer_html

			# Replace <pre> with <figure>.
			# Do this last, because editing with BS4 and pretty printing can muck up
			# spacing in <pre> elements if the elements are removed early
			html = regex.sub(r"<pre data-language=\"([^\"]+?)\">", r"""<figure class="\1 full"><code class="\1 full">""", html)
			html = regex.sub(r"<pre class=\"([^\"]+?)\" data-language=\"([^\"]+?)\">", r"""<figure class="\1 \2 full"><code class="\2 full">""", html)
			html = regex.sub(r"<pre data-language=\"([^\"]+?)\" class=\"([^\"]+?)\">", r"""<figure class="\1 \2 full"><code class="\1 full">""", html)
			html = regex.sub(r"</pre>", r"</code></figure>", html)

			# Fill in <title> elements
			if filename == "index.rst":
				version = regex.findall(r"\.\. version: (.+)", rst)[0]
				html = regex.sub(r"MANUAL_TITLE", "The Standard Ebooks Manual", html)
				html = regex.sub(r"<section id=\".+?\"", r"<section", html)
			else:
				html = regex.sub(r"MANUAL_TITLE", f"{root_number}. {title} - The Standard Ebooks Manual", html)

			# Replace instances of PD_YEAR with PHP echo code
			html = regex.sub(r"PD_YEAR", "<?= PD_YEAR ?>", html)

			with open(Path(work_directory) / filename.replace(".rst", ".php"), "w", encoding="utf-8") as file:
				file.write(html)
				file.truncate()

		# Now, generate the ToC
		toc = natsorted(toc, key=lambda x: x.number)
		toc_html = f"<nav><p><a href=\"/manual/{version}\">The Standard Ebooks Manual of Style</a></p><ol>"
		for toc_item in toc:
			toc_html += f"<li><p><a href=\"/manual/{version}/{toc_item.filename}\">{toc_item.number}. {escape(toc_item.title)}</a></p><ol>"
			for sub_item in toc_item.items:
				toc_html += f"<li><p><a href=\"/manual/{version}/{toc_item.filename}#{sub_item.number}\">{sub_item.number} {escape(sub_item.title)}</a></p></li>"
			toc_html += "</ol></li>"
		toc_html += "</ol></nav>"

		# Place the ToC and version number into the final files
		for filename in os.listdir(work_directory):
			if not filename.endswith(".php"):
				continue

			with open(Path(work_directory) / filename, "r", encoding="utf-8") as file:
				html = file.read()
				html = html.replace("VERSION", version)

				if filename != "index.php":
					html = regex.sub(r"<article(.*?)>", fr"\n{toc_html}\n<article\1>", html)

			# Check if pygments generated any errors (for example, missing quotes in an HTML attribute)
			if "class=\"err\"" in html:
				print(f"Error colorized code in `{filename}`. Search the file for `class=\"err\"`.")

			with open(Path(args.dest_directory) / filename, "w", encoding="utf-8") as file:
				file.write(html)
				file.truncate()

	make_one_page(args.dest_directory)

	return return_code

if __name__ == "__main__":
	sys.exit(main())
