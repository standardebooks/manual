#############################################
Filesystem Layout and File Naming Conventions
#############################################

A bare Standard Ebooks directory structure looks like this:

.. figure:: /images/epub-draft-tree.png
	:alt: A directory tree representing the structure of a bare Standard Ebook.

File locations
**************

#.	XHTML files containing the actual text of the ebook are located in :path:`./src/epub/text/`. All files in this directory end in :path:`.xhtml`.

#.	CSS files used in the ebook are located in :path:`./src/epub/css/`. All files in this directory end in :path:`.css`. This directory contains only two CSS files:

	#.	:path:`./src/epub/css/core.css` is distributed with all ebooks and is not edited.

	#.	:path:`./src/epub/css/local.css` is used for custom CSS local to the particular ebook.

#.	Raw source images used in the ebook, but not distributed with the ebook, are located in :path:`./images/`. These images may be, for example, very high resolution that are later converted to lower resolution for distribution, or raw bitmaps that are later converted to SVG for distribution. Every ebook contains the following images in this directory:

	#.	:path:`./images/titlepage.svg` is the editable titlepage file that is later compiled for distribution.

	#.	:path:`./images/cover.svg` is the editable cover file that is later compiled for distribution.

	#.	:path:`./images/cover.source.(jpg|png|bmp|tif)` is the raw cover art file that may be cropped, resized, or otherwise edited to create :path:`./images/cover.jpg`.

	#.	:path:`./images/cover.jpg` is the final edited cover art that will be compiled into :path:`./src/epub/images/cover.svg` for distribution.

#.	Images compiled or derived from raw source images, that are then distributed with the ebook, are located in :path:`./src/epub/images/`.

#.	The table of contents is located in :path:`./src/epub/toc.xhtml`.

#.	The epub metadata file is located in :path:`./src/epub/content.opf`.

#.	The ONIX metadata file is located in :path:`./src/epub/onix.xml`. This file is identical for all ebooks.

#.	The ONIX metadata file is located in :path:`./src/epub/onix.xml`. This file is identical for all ebooks.

#.	The :path:`./src/META-INF/` and :path:`./src/mimetype` directory and files are epub structural files that are identical for all ebooks.

#.	The :path:`./LICENSE.md` contains the ebook license and is identical for all ebooks.

XHTML file naming conventions
*****************************

#.	Numbers in filenames don’t include leading :path:`0`\s.

#.	Files containing a short story, essay, or other short work in a larger collection, are named with the URL-safe title of the work, excluding any subtitles.

	=============================================================================================== =========================================
	Work                                                                                            Filename
	=============================================================================================== =========================================
	A short story named “The Variable Man”                                                          :path:`the-variable-man.xhtml`
	A short story named “The Sayings of Limpang-Tung (The God of Mirth and of Melodious Minstrels)” :path:`the-sayings-of-limpang-tung.xhtml`
	=============================================================================================== =========================================

#.	Works that are divided into larger parts (sometimes called “parts,” “books,” “volumes,” “sections,” etc.) have their part divisions contained in individual files named after the type of part, followed by a number starting at :path:`1`.

	.. class:: text corrected

		.. compound::

			:path:`book-1.xhtml`

			:path:`book-2.xhtml`

			:path:`part-1.xhtml`

			:path:`part-2.xhtml`

#.	Works that are composed of chapters, short stories, essays, or other short- to medium-length sections have each of those sections in an individual file.

	#.	Chapters *not* contained in separate volumes are named :path:`chapter-N.xhtml`, where :path:`N` is the chapter number starting at :path:`1`.

		================ =========================
		Section          Filename
		================ =========================
		Chapter 1        :path:`chapter-1.xhtml`
		Chapter 2        :path:`chapter-2.xhtml`
		================ =========================

	#.	Chapters contained in separate volumes, where the chapter number re-starts at 1 in each volume, are named :path:`chapter-X-N.xhtml`, where :path:`X` is the part number starting at :path:`1`, and :path:`N` is the chapter number *within the part*, starting at :path:`1`.

		================ =========================
		Section          Filename
		================ =========================
		Part 1           :path:`part-1.xhtml`
		Part 1 Chapter 1 :path:`chapter-1-1.xhtml`
		Part 1 Chapter 2 :path:`chapter-1-2.xhtml`
		Part 1 Chapter 3 :path:`chapter-1-3.xhtml`
		Part 2           :path:`part-2.xhtml`
		Part 2 Chapter 1 :path:`chapter-2-1.xhtml`
		Part 2 Chapter 2 :path:`chapter-2-2.xhtml`
		================ =========================

	#.	Chapters contained in separate volumes, where the chapter number does not re-start at 1 in each volume, are named :path:`chapter-N.xhtml`, where :path:`N` is the chapter number, starting at :path:`1`.

		================ =========================
		Section          Filename
		================ =========================
		Part 1           :path:`part-1.xhtml`
		Chapter 1        :path:`chapter-1.xhtml`
		Chapter 2        :path:`chapter-2.xhtml`
		Chapter 3        :path:`chapter-3.xhtml`
		Part 2           :path:`part-2.xhtml`
		Chapter 4        :path:`chapter-4.xhtml`
		Chapter 5        :path:`chapter-5.xhtml`
		================ =========================

	#.	Works that are composed of extremely short sections, like a volume of short poems, are in a single file containing all of those short sections. The filename is the URL-safe name of the work.

		============================================== =============================
		Section                                        Filename
		============================================== =============================
		A book of short poems called “North of Boston” :path:`north-of-boston.xhtml`
		============================================== =============================

	#.	Frontmatter and backmatter sections have filenames that are named after the type of section, regardless of what the actual title of the section is.

		============================================== =============================
		Section                                        Filename
		============================================== =============================
		A preface titled “Note from the author”        :path:`preface.xhtml`
		============================================== =============================

	#.	If a work contains more than one section of the same type (for example multiple prefaces), the filename is followed by :path:`-N`, where :path:`N` is a number representing the order of the section, starting at :path:`1`.

		=============================================================================== =============================
		Section                                                                         Filename
		=============================================================================== =============================
		The work’s first preface, titled “Preface to the 1850 Edition”                  :path:`preface-1.xhtml`
		The work’s second preface, titled “Preface to the Charles Dickens Edition”      :path:`preface-2.xhtml`
		=============================================================================== =============================

The :path:`se-lint-ignore.xml` file
***********************************

The :bash:`se lint` tool makes best guesses to alert the user to potential issues in an ebook production, and it may sometimes guess wrong. An :path:`se-lint-ignore.xml` file can be placed in the ebook root to make :bash:`se lint` ignore specific error numbers in an ebook.

#.	:bash:`se-lint-ignore.xml` is optional. If it exists, it is in the ebook root.

#.	An empty :bash:`se-lint-ignore.xml` file looks like this:

	.. code:: html

		<?xml version="1.0" encoding="utf-8"?>
		<se-lint-ignore>
		</se-lint-ignore>

#.	The :html:`<se-lint-ignore>` root element contains one or more :html:`<file>` elements.

	#.	:html:`<file>` elements have a :html:`path` attribute containing a filename to match in :path:`./src/epub/text/`.

		.. code:: html

			<file path="chapter-3-1-11.xhtml">
			</file>

	#.	:html:`path` attributes accept shell-style globbing to match files.

		.. code:: html

			<file path="chapter-*.xhtml">
			</file>

	#.	Each :html:`<file>` element contains one or more :html:`<ignore>` elements. Each :html:`<ignore>` element contains one :html:`<code>` element and one :html:`<reason>` element.

		#.	The value of :html:`<code>` is the error/warning code provided by :bash:`se lint`. This code will be ignored for its parent file(s) when :bash:`se lint` is next run.

		#.	The value of :html:`<reason>` is a prose explanation about why the code was ignored. This is to aid future producers or reviewers in understanding the reasoning behind why a code was ignored.

			#.	:html:`<reason>` is required to have a non-whitespace value.

.. class:: no-numbering

Example
=======

The following is an example of a complete :path:`se-lint-ignore.xml` file from :italics:`Tractatus Logico-Philosophicus </ebooks/ludwig-wittgenstein/tractatus-logico-philosophicus/c-k-ogden>`.

.. code:: xml

	<?xml version="1.0" encoding="utf-8"?>
	<se-lint-ignore>
		<file path="introduction.xhtml">
			<ignore>
				<code>t-002</code>
				<reason>Punctuation is deliberately placed outside of quotes in this ebook to prevent confusion with mathematical symbols and formulas.</reason>
			</ignore>
		</file>
		<file path="tractatus-logico-philosophicus.xhtml">
			<ignore>
				<code>s-021</code>
				<reason>The &lt;title&gt; tag is accurate; the work title appears in the half title.</reason>
			</ignore>
			<ignore>
				<code>t-002</code>
				<reason>Punctuation is deliberately placed outside of quotes in this ebook to prevent confusion with mathematical symbols and formulas.</reason>
			</ignore>
		</file>
	</se-lint-ignore>
