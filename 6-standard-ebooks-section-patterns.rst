################################
Standard Ebooks Section Patterns
################################

All Standard Ebooks contain a standardized set of sections that are included in each ebook, and which are usually generated from template files. These sections include sections like the titlepage, imprint, and Uncopyright.

The title string
****************

The title string is a sentence listing the title of the ebook, its author, and any other contributors. It is used in various Standard Ebooks template files.

#.	The title string is formed with the following algorithm.

	-	Start with an empty string.

	-	Append the title of the work, without any subtitles.

	-	Append :string:`, by`, then the author. If there are two authors, separate them with :string:`and`. If there are three or more authors, each one is separated by :string:`,`, and the final one is preceded by :string:`, and`.

	-	If there is a translator, append :string:`. Translated by`, then the translator name. Multiple translators are handled in the same manner as multiple authors.

	-	If there is an illustrator, append :string:`. Illustrated by`, then the illustrator name. Multiple illustrators are handled in the same manner as multiple authors.

#.	While the title string may contain periods, it never ends in a period.

The table of contents
*********************

The table of contents (the ToC) is not viewable as a page in the ebook’s reading order. Instead, the reader’s ereading system displays the ToC as part of its reading interface.

These rules outline how to structure the ToC. Typically, the :bash:`se build-toc` tool constructs the ToC according to these rules, without further changes being necessary.

The :html:`<nav>` element
=============================

#.	The first child of the ToC’s :html:`<body>` element is a :html:`<nav>` element with the semantic inflection :value:`toc`.

#.	The first child of the :html:`<nav>` element is a :html:`<h2 epub:type="title">Table of Contents</h2>` element.

#.	The second child of the :html:`<nav>` element is an :html:`<ol>` element representing the items in the Table of Contents.

The top-level :html:`<ol>` element
----------------------------------

The :html:`<nav>` element’s top-level :html:`<ol>` element contains a list of items in the Table of Contents.

#.	The first child is a link to the titlepage.

	.. code:: html

		<li>
			<a href="text/titlepage.xhtml">Titlepage</a>
		</li>

#.	The second child is a link to the imprint.

	.. code:: html

		<li>
			<a href="text/imprint.xhtml">Imprint</a>
		</li>

#.	The second-to-last child is a link to the colophon.

	.. code:: html

		<li>
			<a href="text/colophon.xhtml">Colophon</a>
		</li>

#.	The last child is a link to the Uncopyright.

	.. code:: html

		<li>
			<a href="text/uncopyright.xhtml">Uncopyright</a>
		</li>

#.	In books with half title pages, the half title page is listed in the ToC and the next sibling is an :html:`<ol>` element containing the book’s contents.

	.. code:: html

		<li>
			<a href="text/halftitlepage.xhtml">The Moon Pool</a>
			<ol>
				<li>
					<a href="text/chapter-1.xhtml"><span epub:type="z3998:roman">I</span>: The Thing on the Moon Path</a>
				</li>
				<li>
					<a href="text/chapter-2.xhtml"><span epub:type="z3998:roman">II</span>: “Dead! All Dead!”</a>
				</li>

	#.	In books that have a half title page, and whose body text is a single file without heading content (for example, `Father Goriot <https://standardebooks.org/ebooks/honore-de-balzac/father-goriot/ellen-marriage>`__ or `The Path to Rome <https://standardebooks.org/ebooks/hilaire-belloc/the-path-to-rome>`__), the half title page ToC entry text is set to :html:`Half-Titlepage`.

	.. code:: html

		<li>
			<a href="text/halftitlepage.xhtml">Half-Titlepage</a>
			<ol>
				<li>
					<a href="text/father-goriot.xhtml">Father Goriot</a>
				</li>

:html:`<li>` descendents
------------------------

#.	Each :html:`<li>` contains an :html:`<a>` element pointing to a file or hash, and optionally also contains an :html:`<ol>` element representing a nested series of ToC items.

#.	If an :html:`<li>` element contains a nested :html:`<ol>` element, that :html:`<li>`’s first child is an :html:`<a>` element that points to the beginning of that section.

	.. code:: html

		<li>
			<a href="text/halftitlepage.xhtml">Sybil</a>
			<ol>
				<li>
					<a href="text/book-1.xhtml">Book <span epub:type="z3998:roman">I</span></a>
					<ol>
						<li>
							<a href="text/chapter-1-1.xhtml" epub:type="z3998:roman">I</a>
						</li>

#.	Roman numerals in the ToC have a :html:`<span>` element if the entire contents of the :html:`<a>` element are not a Roman numeral.

	.. class:: wrong

		.. code:: html

			<li>
				<a href="text/chapter-1.xhtml">I</a>
			</li>

	.. class:: wrong

		.. code:: html

			<li>
				<a href="text/chapter-1.xhtml"><span epub:type="z3998:roman">I</span></a>
			</li>

	.. class:: corrected

		.. code:: html

			<li>
				<a href="text/chapter-1.xhtml" epub:type="z3998:roman">I</a>
			</li>

	.. class:: corrected

		.. code:: html

			<li>
				<a href="text/book-1.xhtml">Book <span epub:type="z3998:roman">I</span></a>
				<ol>
					...
				</ol>
			</li>

:html:`<a>` descendents
-----------------------

#.	The :value:`title`, :value:`subtitle`, :value:`ordinal`, and any `related title epub semantics <https://www.w3.org/TR/epub-ssv-11/#sec-titles>`__ are not included in ToC entries. Their usage context is only within actual heading content.

#.	The text of the :html:`<a>` element is decided as follows:

	1.	If there is no :html:`<hgroup>` in the section, the text becomes the inner XHTML of the top :html:`<h1>`–:html:`<h6>` element with any of the above semantics removed.

	2.	If there is an :html:`<hgroup>` element:

		1.	If the :html:`<hgroup>`’s closest parent :html:`<section>` or :html:`<article>` has an :html:`epub:type` value of :value:`part`, :value:`division`, or :value:`volume`, then keep all :html:`<hgroup>` children.

		2.	Otherwise, if the :html:`<hgroup>`’s closest parent :html:`<section>` or :html:`<article>` has an :html:`epub:type` value of :value:`halftitlepage`, or if the first child of the :html:`<hgroup>` has the :value:`title` semantic, then discard any children with the :value:`subtitle` semantic.

		3.	Then, the text becomes the inner XHTML of the first :html:`<hgroup>` child. If there is a second child, append a colon and space to the text, then the inner XHTML of the second child. The above semantics are then removed.

Examples
~~~~~~~~

.. code:: html

	<article id="a-daughter-of-albion" epub:type="se:short-story">
		<h2 epub:type="title">A Daughter of Albion</h2>
		<p>...</p>
	</article>

Result: :html:`A Daughter of Albion`

.. code:: html

	<section id="book-1" epub:type="part">
		<hgroup>
			<h2>
				<span epub:type="label">Book</span>
				<span epub:type="ordinal z3998:roman">I</span>
			</h2>
			<p epub:type="title">The Coming of the Martians</p>
		</hgroup>
		<p>...</p>
	</section>

Result: :html:`Book <span epub:type="z3998:roman">I</span>: The Coming of the Martians`

.. code:: html

	<section id="chapter-1" epub:type="chapter">
		<hgroup>
			<h2 epub:type="ordinal z3998:roman">I</h2>
			<p epub:type="title">A Fellow Traveller</p>
		</hgroup>
		<p>...</p>
	</section>

Result: :html:`<span epub:type="z3998:roman">I</span>: A Fellow Traveller`

.. code:: html

	<section id="epilogue" epub:type="epilogue">
		<hgroup>
			<h3 epub:type="title">Epilogue</h3>
			<p epub:type="subtitle">A Morning Call</p>
		</hgroup>
		<p>...</p>
	</section>

Result: :html:`Epilogue`

The landmarks :html:`<nav>` element
===================================

After the first :html:`<nav>` element, there is a second :html:`<nav>` element with the semantic inflection of :value:`landmarks`.

#.	The first child is an :html:`<h2 epub:type="title">Landmarks</h2>` element.

#.	The second child is an :html:`<ol>` element listing the major structural divisions of the book.

:html:`<li>` descendents
------------------------

Each :html:`<li>` element contains a link to either the start of the main text (i.e. the start of the bodymatter, excluding a half titlepage), or to a major reference section (i.e. backmatter including endnotes, bibliography, glossary, index, LoI, etc.). `See the IDPF a11y best practices document <http://idpf.org/epub/a11y/techniques/#sem-003>`__ for more information.

#.	Each :html:`<li>` element has the computed semantic inflection of top-level :html:`<section>` element in the file. The computed semantic inflection includes inherited semantic inflection from the :html:`<body>` element.

	.. code:: html

		<li>
			<a href="text/endnotes.xhtml" epub:type="backmatter endnotes">Endnotes</a>
		</li>

#.	The body text, as a single unit regardless of internal divisions, is represented by a link to the first file of the body text. In a prose novel, this is usually Chapter 1 or Part 1. In a collection this is usually the first item, like the first short story in a short story collection. The text is the title of the work as represented in the metadata :html:`<dc:title>` element.

	.. code:: html

		<li>
			<a href="text/book-1.xhtml" epub:type="bodymatter z3998:fiction">Sybil</a>
		</li>

	.. code:: html

		<li>
			<a href="text/chapter-1.xhtml" epub:type="bodymatter z3998:fiction">The Moon Pool</a>
		</li>

	.. code:: html

		<li>
			<a href="text/the-adventure-of-wisteria-lodge.xhtml" epub:type="bodymatter z3998:fiction">His Last Bow</a>
		</li>

The titlepage
*************

#.	The Standard Ebooks titlepage is the first item in the ebook’s content flow. Standard Ebooks do not have a separate cover page file within the content flow.

#.	The title page has a :html:`<title>` element with the value :string:`Titlepage`.

#.	The titlepage contains one :html:`<section id="titlepage" epub:type="titlepage">` element which in turn contains one :html:`<h1 epub:type="title">` element, author information, as well as one :html:`<img src="../images/titlepage.svg">` element.

#.	The titlepage does not contain the subtitle, if there is one.

#.	The :html:`<img>` element has an empty :html:`alt` attribute.

#.	A complete titlepage looks like the following template:

	.. code:: html

		<?xml version="1.0" encoding="utf-8"?>
		<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" epub:prefix="z3998: http://www.daisy.org/z3998/2012/vocab/structure/, se: https://standardebooks.org/vocab/1.0" xml:lang="en-US">
			<head>
				<title>Titlepage</title>
				<link href="../css/core.css" rel="stylesheet" type="text/css"/>
				<link href="../css/local.css" rel="stylesheet" type="text/css"/>
			</head>
			<body epub:type="frontmatter">
				<section id="titlepage" epub:type="titlepage">
					<h1 epub:type="title">TITLE</h1>
					<p>By <b epub:type="z3998:author">AUTHOR</b>.</p>
					<p>Translated by <b epub:type="z3998:translator">TRANSLATOR</b>.</p>
					<p>Illustrated by <b>ILLUSTRATOR</b>.</p>
					<img alt="" src="../images/titlepage.svg" epub:type="se:image.color-depth.black-on-transparent"/>
				</section>
			</body>
		</html>

The imprint
***********

#.	The Standard Ebooks imprint is the second item in the ebook’s content flow.

#.	The imprint has a :html:`<title>` element with the value :string:`Imprint`.

#.	The imprint contains one :html:`<section id="imprint" epub:type="imprint">` element, which in turn contains one :html:`<header>` element with the Standard Ebooks logo, followed by a series of :html:`<p>` elements containing the imprint’s content.

#.	The second :html:`<p>` element contains links to the online transcription that the ebook is based off of, followed by a link to the online page scans used to proof against.

	#.	While the template lists Project Gutenberg and the Internet Archive as the default sources for transcriptions and scans, these may be adjusted to the specific sources used for a particular ebook.

	#.	When a source is preceded by “the”, “the” is outside of the link to the source.

		.. class:: wrong

			.. code:: html

				<p>This particular ebook is based on digital scans from <a href="IA_URL">the Internet Archive</a>.</p>

		.. class:: corrected

			.. code:: html

				<p>This particular ebook is based on digital scans from the <a href="IA_URL">Internet Archive</a>.</p>

	#.	If an ebook is based on multiple sources or transcriptions (for example, a short story collection of a voluminous author), then the source sentence is altered to reflect that either the transcriptions, the page scans, or both, came from various sources.

		#. If transcriptions or page scans come from the same domain (like only the Internet Archive or HathiTrust):

			.. code:: html

				<p>This particular ebook is based on transcriptions from <a href="EBOOK_URL#transcriptions">Project Gutenberg</a> and on digital scans from the <a href="IA_URL">Internet Archive</a>.</p>

			.. code:: html

				<p>This particular ebook is based on a transcription from <a href="PG_URL">Project Gutenberg</a> and on digital scans from the <a href="EBOOK_URL#page-scans">Internet Archive</a>.</p>

			.. code:: html

				<p>This particular ebook is based on transcriptions from <a href="EBOOK_URL#transcriptions">Project Gutenberg</a> and on digital scans from the <a href="EBOOK_URL#page-scans">Internet Archive</a>.</p>

		#. If transcriptions or page scans come from more than one domain (like both the Internet Archive and HathiTrust):

			.. code:: html

				<p>This particular ebook is based on transcriptions from <a href="EBOOK_URL#transcriptions">various sources</a> and on digital scans from the <a href="IA_URL">Internet Archive</a>.</p>

			.. code:: html

				<p>This particular ebook is based on a transcription from <a href="PG_URL">Project Gutenberg</a> and on digital scans from <a href="EBOOK_URL#page-scans">various sources</a>.</p>

			.. code:: html

				<p>This particular ebook is based on transcriptions from <a href="EBOOK_URL#transcriptions">various sources</a> and on digital scans from <a href="EBOOK_URL#page-scans">various sources</a>.</p>

#.	A complete imprint looks like the following template:

	.. code:: html

		<?xml version="1.0" encoding="utf-8"?>
		<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" epub:prefix="z3998: http://www.daisy.org/z3998/2012/vocab/structure/, se: https://standardebooks.org/vocab/1.0" xml:lang="en-US">
			<head>
				<title>Imprint</title>
				<link href="../css/core.css" rel="stylesheet" type="text/css"/>
				<link href="../css/local.css" rel="stylesheet" type="text/css"/>
			</head>
			<body epub:type="frontmatter">
				<section id="imprint" epub:type="imprint">
					<header>
						<h2 epub:type="title">Imprint</h2>
						<img alt="The Standard Ebooks logo" src="../images/logo.svg" epub:type="z3998:publisher-logo se:image.color-depth.black-on-transparent"/>
					</header>
					<p>This ebook is the product of many hours of hard work by volunteers for <a href="https://standardebooks.org">Standard Ebooks</a>, and builds on the hard work of other literature lovers made possible by the public domain.</p>
					<p>This particular ebook is based on a transcription from <a href="PG_URL">Project Gutenberg</a> and on digital scans from the <a href="IA_URL">Internet Archive</a>.</p>
					<p>The writing and artwork within are believed to be in the <abbr>U.S.</abbr> public domain, and Standard Ebooks releases this ebook edition under the terms in the <a href="https://creativecommons.org/publicdomain/zero/1.0/">CC0 1.0 Universal Public Domain Dedication</a>. For full license information, see the <a href="uncopyright.xhtml">Uncopyright</a> at the end of this ebook.</p>
					<p>Standard Ebooks is a volunteer-driven project that produces ebook editions of public domain literature using modern typography, technology, and editorial standards, and distributes them free of cost. You can download this and other ebooks carefully produced for true book lovers at <a href="https://standardebooks.org">standardebooks.org</a>.</p>
				</section>
			</body>
		</html>

The half title page
*******************

#.	A half title page is included when there is front matter of any type in an ebook besides the titlepage and imprint.

#.	The half title page is located after the last item of front matter, before the body matter.

#.	The half title page has a :html:`<title>` element containing the full title of the ebook.

#.	The half title page contains one :html:`<section id="halftitlepage" epub:type="halftitlepage">` element, which in turn contains either one :html:`<h2 epub:type="fulltitle">` element containing the full title of the ebook, or one :html:`<hgroup epub:type="fulltitle">` element containing one :html:`<h2 epub:type="title">` element and one :html:`<p epub:type="subtitle">` element.

#.	If the ebook has a subtitle, it is included in the half title page.

#.	The :value:`fulltitle` semantic is applied to the top-level heading element in the half title page. This is usually either :html:`<hgroup>` in works with subtitles or :html:`<h2>` in works without.

#.	Formatting for the :html:`<h2>` element follows patterns in `7.2.9 </manual/VERSION/7-high-level-structural-patterns#7.2.9>`__.

#.	A complete half title page looks like the following template:

	.. code:: html

		<?xml version="1.0" encoding="utf-8"?>
		<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" epub:prefix="z3998: http://www.daisy.org/z3998/2012/vocab/structure/, se: https://standardebooks.org/vocab/1.0" xml:lang="en-GB">
			<head>
				<title>His Last Bow</title>
				<link href="../css/core.css" rel="stylesheet" type="text/css"/>
				<link href="../css/local.css" rel="stylesheet" type="text/css"/>
			</head>
			<body epub:type="frontmatter">
				<section id="halftitlepage" epub:type="halftitlepage">
					<hgroup epub:type="fulltitle">
						<h2 epub:type="title">His Last Bow</h2>
						<p epub:type="subtitle">Some Reminiscences of Sherlock Holmes</p>
					</hgroup>
				</section>
			</body>
		</html>

The colophon
************

#.	The colophon is the second-to-last item in the ebook’s content flow.

#.	The colophon has a :html:`<title>` element with the value :string:`Colophon`.

#.	The colophon contains one :html:`<section id="colophon" epub:type="colophon">` element, which in turn contains one :html:`<header>` element with the Standard Ebooks logo, followed by a series of :html:`<p>` elements containing the colophon’s content.

Names
=====

#.	Within :html:`<p>` elements, proper names except for the book title and cover art title are wrapped in an :html:`<a>` element pointing to the name’s Wikipedia page, or to a link representing the name, like a personal homepage.

#.	If a name does not have an English-language Wikipedia entry, the name is wrapped in :html:`<b epub:type="z3998:personal-name">`.

#.	Two names are separated by :string:`and`. Three or more names are separated by commas, with the final name separated by :string:`, and`. (I.e., with an Oxford comma.)

	.. class:: wrong

		.. code:: html

			<b epub:type="z3998:personal-name">Fritz Ohrenschall</b>, <b epub:type="z3998:personal-name">Sania Ali Mirza</b> and <a href="https://www.pgdp.net">The Online Distributed Proofreading Team</a>

	.. class:: corrected

		.. code:: html

			<b epub:type="z3998:personal-name">Fritz Ohrenschall</b>, <b epub:type="z3998:personal-name">Sania Ali Mirza</b>, and <a href="https://www.pgdp.net">The Online Distributed Proofreading Team</a>

Anonymous contributors
----------------------

#.	Anonymous or unknown primary contributors (like the author or cover artist) are listed as :html:`<b>Anonymous</b>`.

#.	Anonymous volunteers working on digitization or the actual ebook production are listed as :html:`<b>An Anonymous Volunteer</b>`. Note that their *metadata entries* are still listed as :string:`Anonymous`, even though their *colophon entries* differ.

#.	Both types of volunteer string are not names, therefore their parent :html:`<b>` elements do not have name semantics.

Sponsors
========

#.	An ebook may have a financial sponsor. If so, the following block:

		.. code:: html

			<p>This ebook was produced for<br/>
			<a href="https://standardebooks.org">Standard Ebooks</a><br/>
			by<br/>

	is replaced with:

		.. code:: html

			<p><a href="SPONSOR_HOMEPAGE_URL">SPONSOR_NAME</a><br/>
			sponsored the production of this ebook for<br/>
			<a href="https://standardebooks.org">Standard Ebooks</a>.<br/>
			It was produced by<br/>

Subsections
===========

#.	Subsections are represented by a :html:`<p>` element.

	#.	Within each :html:`<p>` element, a :html:`<br/>` element is placed before and after any proper name block. A proper name block may contain more than one name in a direct series (like a list of transcribers).

		.. code:: html

			<p><i epub:type="se:name.publication.book">The Moon Pool</i><br/>
			was published in 1919 by<br/>
			<a href="https://en.wikipedia.org/wiki/Abraham_Merritt">Abraham Merritt</a>.</p>

	#.	The first :html:`<p>` block names the book, its publication year, and its author.

		.. code:: html

			<p><i epub:type="se:name.publication.book">The Moon Pool</i><br/>
			was published in 1919 by<br/>
			<a href="https://en.wikipedia.org/wiki/Abraham_Merritt">Abraham Merritt</a>.</p>

		#.	If the book has a translator, a translator block follows the author name in the same :html:`<p>` element. The translator block follows this formula: :string:`It was translated from LANGUAGE in YEAR by <a href="TRANSLATOR_WIKI_URL">TRANSLATOR</a>.`.

			.. code:: html

				<p><i epub:type="se:name.publication.book">Eugene Onegin</i><br/>
				was published in 1837 by<br/>
				<a href="https://en.wikipedia.org/wiki/Alexander_Pushkin">Alexander Pushkin</a>.<br/>
				It was translated from Russian in 1881 by<br/>
				<a href="https://en.wikipedia.org/wiki/Henry_S._Spalding">Henry Spalding</a>.</p>

	#.	The second :html:`<p>` block names the Standard Ebooks producer, the original transcribers, and the page scan sources.

		.. code:: html

			<p>This ebook was produced for<br/>
			<a href="https://standardebooks.org">Standard Ebooks</a><br/>
			by<br/>
			<a href="https://www.robinwhittleton.com/">Robin Whittleton</a>,<br/>
			and is based on a transcription produced in 1997 by<br/>
			<b>An Anonymous Volunteer</b> and <b epub:type="z3998:personal-name">David Widger</b><br/>
			for<br/>
			<a href="https://www.gutenberg.org/ebooks/965">Project Gutenberg</a><br/>
			and on digital scans from the<br/>
			<a href="https://archive.org/details/worksofdumas24dumaiala">Internet Archive</a>.</p>

		#.	If the Standard ebooks producer also transcribed the book *in its entirety*, then the first line becomes: :html:`<p>This ebook was transcribed and produced for<br/>`.

		#.	If an ebook is based on multiple sources or transcriptions (for example, a short story collection of a voluminous author), then the source sentence is altered to reflect that either the transcriptions, the page scans, or both, came from various sources. Individual transcriber names are omitted.

			#.	If the transcriptions or page scans all came from the same source (i.e., all of the transcriptions came from Project Gutenberg):

				.. code:: html

					<p>This ebook was produced for<br/>
					<a href="https://standardebooks.org">Standard Ebooks</a><br/>
					by<br/>
					<a href="https://www.robinwhittleton.com/">Robin Whittleton</a>,<br/>
					and is based on transcriptions from<br/>
					<a href="EBOOK_URL#transcriptions">Project Gutenberg</a><br/>
					and on digital scans from the<br/>
					<a href="https://archive.org/details/worksofdumas24dumaiala">Internet Archive</a>.</p>

				.. code:: html

					<p>This ebook was produced for<br/>
					<a href="https://standardebooks.org">Standard Ebooks</a><br/>
					by<br/>
					<a href="https://www.robinwhittleton.com/">Robin Whittleton</a>,<br/>
					and is based on a transcription produced in 1997 by<br/>
					<b>An Anonymous Volunteer</b> and <b epub:type="z3998:personal-name">David Widger</b><br/>
					for<br/>
					<a href="https://www.gutenberg.org/ebooks/965">Project Gutenberg</a><br/>
					and on digital scans from the<br/>
					<a href="EBOOK_URL#page-scans">Internet Archive</a>.</p>


				.. code:: html

					<p>This ebook was produced for<br/>
					<a href="https://standardebooks.org">Standard Ebooks</a><br/>
					by<br/>
					<a href="https://www.robinwhittleton.com/">Robin Whittleton</a>,<br/>
					and is based on transcriptions from<br/>
					<a href="EBOOK_URL#transcriptions">Project Gutenberg</a><br/>
					and on digital scans from the<br/>
					<a href="EBOOK_URL#page-scans">Internet Archive</a>.</p>

			#.	If the transcriptions or page scans came from different sources:

				.. code:: html

					<p>This ebook was produced for<br/>
					<a href="https://standardebooks.org">Standard Ebooks</a><br/>
					by<br/>
					<a href="https://www.robinwhittleton.com/">Robin Whittleton</a>,<br/>
					and is based on transcriptions from <br/>
					<a href="EBOOK_URL#transcriptions">various sources</a><br/>
					and on digital scans from the<br/>
					<a href="https://archive.org/details/worksofdumas24dumaiala">Internet Archive</a>.</p>

				.. code:: html

					<p>This ebook was produced for<br/>
					<a href="https://standardebooks.org">Standard Ebooks</a><br/>
					by<br/>
					<a href="https://www.robinwhittleton.com/">Robin Whittleton</a>,<br/>
					and is based on a transcription produced in 1997 by<br/>
					<b>An Anonymous Volunteer</b> and <b epub:type="z3998:personal-name">David Widger</b><br/>
					for<br/>
					<a href="https://www.gutenberg.org/ebooks/965">Project Gutenberg</a><br/>
					and on digital scans from<br/>
					<a href="EBOOK_URL#page-scans">various sources</a>.</p>

				.. code:: html

					<p>This ebook was produced for<br/>
					<a href="https://standardebooks.org">Standard Ebooks</a><br/>
					by<br/>
					<a href="https://www.robinwhittleton.com/">Robin Whittleton</a>,<br/>
					and is based on transcriptions from<br/>
					<a href="EBOOK_URL#transcriptions">various sources</a><br/>
					and on digital scans from<br/>
					<a href="EBOOK_URL#page-scans">various sources</a>.</p>

	#.	The third :html:`<p>` block names the cover art, cover artist, and the typefaces used on the cover and title pages.

		.. code:: html

			<p>The cover page is adapted from<br/>
			<i epub:type="se:name.visual-art.painting">Floral Still Life</i>,<br/>
			a painting completed in 1639 by<br/>
			<a href="https://en.wikipedia.org/wiki/Hans_Gillisz._Bollongier">Hans Bollongier</a>.<br/>
			The cover and title pages feature the<br/>
			<b epub:type="se:name.visual-art.typeface">League Spartan</b> and <b epub:type="se:name.visual-art.typeface">Sorts Mill Goudy</b><br/>
			typefaces created in 2014 and 2009 by<br/>
			<a href="https://www.theleagueofmoveabletype.com">The League of Moveable Type</a>.</p>

	#.	The fourth :html:`<p>` block lists the original release date of the ebook and its Standard Ebooks page URL.

		.. code:: html

			<p>The first edition of this ebook was released on<br/>
			<b>May 11, 2018, 2:13 <abbr class="eoc">a.m.</abbr></b><br/>
			You can check for updates to this ebook, view its revision history, or download it for different ereading systems at<br/>
			<a href="https://standardebooks.org/ebooks/alexandre-dumas/the-black-tulip/p-f-collier-and-son">standardebooks.org/ebooks/alexandre-dumas/the-black-tulip/p-f-collier-and-son</a>.</p>

	#.	The fifth :html:`<p>` block is a short formula inviting volunteers.

		.. code:: html

			<p>The volunteer-driven Standard Ebooks project relies on readers like you to submit typos, corrections, and other improvements. Anyone can contribute at <a href="https://standardebooks.org">standardebooks.org</a>.</p>

.. class:: no-numbering

An example of a complete colophon
=================================

.. code:: html

	<?xml version="1.0" encoding="utf-8"?>
	<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" epub:prefix="z3998: http://www.daisy.org/z3998/2012/vocab/structure/, se: https://standardebooks.org/vocab/1.0" xml:lang="en-US">
		<head>
			<title>Colophon</title>
			<link href="../css/core.css" rel="stylesheet" type="text/css"/>
			<link href="../css/local.css" rel="stylesheet" type="text/css"/>
		</head>
		<body epub:type="backmatter">
			<section id="colophon" epub:type="colophon">
				<header>
					<h2 epub:type="title">Colophon</h2>
					<img alt="The Standard Ebooks logo" src="../images/logo.svg" epub:type="z3998:publisher-logo se:image.color-depth.black-on-transparent"/>
				</header>
				<p><i epub:type="se:name.publication.book">The Black Tulip</i><br/>
				was published in 1850 by<br/>
				<a href="https://en.wikipedia.org/wiki/Alexandre_Dumas">Alexandre Dumas</a>.<br/>
				It was translated from French in 1902 by<br/>
				<a href="https://en.wikipedia.org/wiki/Peter_F._Collier"><abbr epub:type="z3998:given-name">P. F.</abbr> Collier and Son</a>.</p>
				<p>This ebook was produced for<br/>
				<a href="https://standardebooks.org">Standard Ebooks</a><br/>
				by<br/>
				<a href="https://www.robinwhittleton.com/">Robin Whittleton</a>,<br/>
				and is based on a transcription produced in 1997 by<br/>
				<b>An Anonymous Volunteer</b> and <b epub:type="z3998:personal-name">David Widger</b><br/>
				for<br/>
				<a href="https://www.gutenberg.org/ebooks/965">Project Gutenberg</a><br/>
				and on digital scans from the<br/>
				<a href="https://archive.org/details/worksofdumas24dumaiala">Internet Archive</a>.</p>
				<p>The cover page is adapted from<br/>
				<i epub:type="se:name.visual-art.painting">Floral Still Life</i>,<br/>
				a painting completed in 1639 by<br/>
				<a href="https://en.wikipedia.org/wiki/Hans_Gillisz._Bollongier">Hans Bollongier</a>.<br/>
				The cover and title pages feature the<br/>
				<b epub:type="se:name.visual-art.typeface">League Spartan</b> and <b epub:type="se:name.visual-art.typeface">Sorts Mill Goudy</b><br/>
				typefaces created in 2014 and 2009 by<br/>
				<a href="https://www.theleagueofmoveabletype.com">The League of Moveable Type</a>.</p>
				<p>The first edition of this ebook was released on<br/>
				<b>May 11, 2018, 2:13 <abbr class="eoc">a.m.</abbr></b><br/>
				You can check for updates to this ebook, view its revision history, or download it for different ereading systems at<br/>
				<a href="https://standardebooks.org/ebooks/alexandre-dumas/the-black-tulip/p-f-collier-and-son">standardebooks.org/ebooks/alexandre-dumas/the-black-tulip/p-f-collier-and-son</a>.</p>
				<p>The volunteer-driven Standard Ebooks project relies on readers like you to submit typos, corrections, and other improvements. Anyone can contribute at <a href="https://standardebooks.org">standardebooks.org</a>.</p>
			</section>
		</body>
	</html>

The Uncopyright
***************

Where traditionally published ebooks may contain a copyright page at the front of the ebook, Standard Ebooks contain an Uncopyright page at the end of the ebook.

#.	The Uncopyright page is the last item in the ebook’s content flow.

#.	The Uncopyright page follows the template created by :bash:`se create-draft` exactly.
