################################
Standard Ebooks Section Patterns
################################

All Standard Ebooks set of sections that are included in each ebook, and which are usually generated from template files. These sections include sections like the titlepage, imprint, and Uncopyright.

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

These rules outline how to structure the ToC. Typically, the :bash:`se print-toc` tool constructs the ToC according to these rules, without further changes being necessary.

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

#.	The second-to-last child is a link to the Uncopyright.

	.. code:: html

		<li>
			<a href="text/uncopyright.xhtml">Uncopyright</a>
		</li>

#.	In books with half title pages, the half title page is listed in the ToC and the next sibling is an :html:`<ol>` element containing the book’s contents.

	.. code:: html

		<li>
			<a href="text/halftitle.xhtml">The Moon Pool</a>
			<ol>
				<li>
					<a href="text/chapter-1.xhtml"><span epub:type="z3998:roman">I</span>: The Thing on the Moon Path</a>
				</li>
				<li>
					<a href="text/chapter-2.xhtml"><span epub:type="z3998:roman">II</span>: “Dead! All Dead!”</a>
				</li>

:html:`<li>` descendents
------------------------

#.	Each :html:`<li>` contains an :html:`<a>` element pointing to a file or hash, and optionally also contains an :html:`<ol>` element representing a nested series of ToC items.

#.	If an :html:`<li>` element contains a nested :html:`<ol>` element, that :html:`<li>`’s first child is an :html:`<a>` element that points to the beginning of that section.

	.. code:: html

		<li>
			<a href="text/halftitle.xhtml">Sybil</a>
			<ol>
				<li>
					<a href="text/book-1.xhtml">Book <span epub:type="z3998:roman">I</span></a>
					<ol>
						<li>
							<a href="text/chapter-1-1.xhtml" epub:type="z3998:roman">I</a>
						</li>

#.	Roman numerals in the ToC have the semantic inflection of :value:`z3998:roman`. A :html:`<span>` element is included if the entire contents of the :html:`<a>` element are not a Roman numeral.

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

#.	The :value:`title`, :value:`subtitle`, :title:`ordinal`, and any `related title epub semantics <https://idpf.github.io/epub-vocabs/structure/#titles>`__ are not included in ToC entries. Their usage context is only within actual heading content.

#.	Chapters without titles are represented by their Roman ordinal, without the word :string:`Chapter`.

	.. code:: html

		<a href="text/chapter-11.xhtml" epub:type="z3998:roman">XI</a>

#.	Chapters with titles are represented by their Roman ordinal, followed by a colon and a space, followed by the chapter title.

	.. code:: html

		<a href="text/chapter-3.xhtml"><span epub:type="z3998:roman">III</span>: The Moon Rock</a>

#.	Chapters with unique identifiers (i.e. not :string:`Chapter`, but something unique to the style of the book, like :string:`Book` or :string:`Stave`), include that unique identifier in the :html:`<a>` element.

	.. code:: html

		<a href="text/chapter-1.xhtml">Stave <span epub:type="z3998:roman">I</span>: Marley’s Ghost</a>

#.	High-level sections (like parts or divisions) without titles are represented by their identifier (like :string:`Book` or :string:`Part`), followed by their Roman ordinal.

	.. code:: html

		<a href="text/book-1.xhtml">Book <span epub:type="z3998:roman">I</span></a>

#.	High-level sections (like parts or divisions) with titles include the title.

	.. code:: html

		<a href="text/book-10.xhtml">Book <span epub:type="z3998:roman">X</span>: The Boys</a>

#.	Sections that are not chapters do not include their subtitles in the ToC.

	.. class:: wrong

		.. code:: html

			<a href="text/epilogue.xhtml">Epilogue: A Morning Call</a>

	.. class:: corrected

		.. code:: html

			<a href="text/epilogue.xhtml">Epilogue</a>

#.	High-level sections (like parts or divisions) with titles include the title.

	.. code:: html

		<a href="text/book-10.xhtml">Book <span epub:type="z3998:roman">X</span>: The Boys</a>

#.	Entries for half title pages do not include the subtitle.

	.. code:: html

		<li>
			<a href="text/halftitle.xhtml">His Last Bow</a>
			<ol>
				...
			</ol>
		</li>

The landmarks :html:`<nav>` element
===================================

After the first :html:`<nav>` element, there is a second :html:`<nav>` element with the semantic inflection of :value:`landmarks`.

#.	The first child is an :html:`<h2 epub:type="title">Landmarks</h2>` element.

#.	The second child is an :html:`<ol>` element listing the major structural divisions of the book.

:html:`<li>` descendents
------------------------

Each :html:`<li>` element contains a link to one of the major structural divisions of the book. In general, a structural division is any section of the book that is not part of the body text, plus one element representing the beginning of the body text.

#.	Each :html:`<li>` element has the computed semantic inflection of top-level :html:`<section>` element in the file. The computed semantic inflection includes inherited semantic inflection from the :html:`<body>` element.

	.. code:: html

		<li>
			<a href="text/preface.xhtml" epub:type="frontmatter preface">Preface</a>
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

#.	The titlepage contains one :html:`<section id="titlepage" epub:type="titlepage">` element which in turn contains one :html:`<img src="../images/titlepage.svg">` element.

#.	The :html:`<img>` element has its :html:`alt` attribute set to :string:`The titlepage for the Standard Ebooks edition of TITLE_STRING`, where :string:`TITLE_STRING` is the `Standard Ebooks title string </manual/VERSION/6-standard-ebooks-sectoin-patterns#6.1>`__ for the ebook.

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
					<img alt="The titlepage for the Standard Ebooks edition of TITLE_STRING" src="../images/titlepage.svg" epub:type="se:color-depth.black-on-transparent"/>
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

				<p>This particular ebook is based on digital scans available at <a href="IA_URL">the Internet Archive</a>.</p>

		.. class:: corrected

			.. code:: html

				<p>This particular ebook is based on digital scans available at the <a href="IA_URL">Internet Archive</a>.</p>

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
						<img alt="The Standard Ebooks logo" src="../images/logo.svg" epub:type="z3998:publisher-logo se:color-depth.black-on-transparent"/>
					</header>
					<p>This ebook is the product of many hours of hard work by volunteers for <a href="https://standardebooks.org">Standard Ebooks</a>, and builds on the hard work of other literature lovers made possible by the public domain.</p>
					<p>This particular ebook is based on a transcription produced for <a href="PG_URL">Project Gutenberg</a> and on digital scans available at the <a href="IA_URL">Internet Archive</a>.</p>
					<p>The writing and artwork within are believed to be in the <abbr>U.S.</abbr> public domain, and Standard Ebooks releases this ebook edition under the terms in the <a href="https://creativecommons.org/publicdomain/zero/1.0/">CC0 1.0 Universal Public Domain Dedication</a>. For full license information, see the <a href="uncopyright.xhtml">Uncopyright</a> at the end of this ebook.</p>
					<p>Standard Ebooks is a volunteer-driven project that produces ebook editions of public domain literature using modern typography, technology, and editorial standards, and distributes them free of cost. You can download this and other ebooks carefully produced for true book lovers at <a href="https://standardebooks.org">standardebooks.org</a>.</p>
				</section>
			</body>
		</html>

The half title page
*******************

#.	A half title page is included when there is front matter of any type in an ebook besides the titlepage and imprint.

#.	The half title page located after the last item of front matter, before the body matter.

#.	The half title page has a :html:`<title>` element with the value :string:`Half Title`.

#.	The half title page contains one :html:`<section id="halftitlepage" epub:type="halftitlepage">` element, which in turn contains one :html:`<h1 epub:type="fulltitle">` element containing the full title of the ebook, including subtitles. The half title page is the only place where an :html:`<h1>` element may appear in a Standard Ebook.

#.	Formatting for the :html:`<h1>` element follows patterns in `7.2.6.7 </manual/VERSION/7-high-level-structural-patterns#7.2.6.7>`__ and `7.2.6.8 </manual/VERSION/7-high-level-structural-patterns#7.2.6.8>`__.

#.	A complete half title page looks like the following template:

	.. code:: html

		<?xml version="1.0" encoding="utf-8"?>
		<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" epub:prefix="z3998: http://www.daisy.org/z3998/2012/vocab/structure/, se: https://standardebooks.org/vocab/1.0" xml:lang="en-GB">
			<head>
				<title>Half Title</title>
				<link href="../css/core.css" rel="stylesheet" type="text/css"/>
				<link href="../css/local.css" rel="stylesheet" type="text/css"/>
			</head>
			<body epub:type="frontmatter">
				<section id="halftitlepage" epub:type="halftitlepage">
					<h1 epub:type="fulltitle">
						<span epub:type="title">His Last Bow</span>
						<span epub:type="subtitle">Some Reminiscences of Sherlock Holmes</span>
					</h1>
				</section>
			</body>
		</html>

The colophon
************

#.	The colophon is the second-to-last item in the ebook’s content flow.

#.	The colophon has a :html:`<title>` element with the value :string:`Colophon`.

#.	The half title page contains one :html:`<section id="colophon" epub:type="colophon">` element, which in turn contains one :html:`<header>` element with the Standard Ebooks logo, followed by a series of :html:`<p>` elements containing the colophon’s content.

Names
=====

#.	Within :html:`<p>` elements, proper names except for the book title and cover art title are wrapped in an :html:`<a>` element pointing to the name’s Wikipedia page, or to a link representing the name, like a personal homepage.

#.	If a name does not have a Wikipedia entry, the name is wrapped in :html:`<b class="name">`.

#.	Two names are separated by :string:`and`. Three or more names are separated by commas, with the final name separated by :string:`, and`. (I.e., with an Oxford comma.)

	.. class:: wrong

		.. code:: html

			<b class="name">Fritz Ohrenschall</b>, <b class="name">Sania Ali Mirza</b> and <a href="https://www.pgdp.net">The Online Distributed Proofreading Team</a>

	.. class:: corrected

		.. code:: html

			<b class="name">Fritz Ohrenschall</b>, <b class="name">Sania Ali Mirza</b>, and <a href="https://www.pgdp.net">The Online Distributed Proofreading Team</a>

#.	Any anonymous contributor is listed as :string:`An Anonymous Volunteer`.

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
				<b class="name">Henry Spalding</b>.</p>

	#.	The second :html:`<p>` block names the Standard Ebooks producer, the original transcribers, and the page scan sources.

		.. code:: html

			<p>This ebook was produced for the<br/>
			<a href="https://standardebooks.org">Standard Ebooks project</a><br/>
			by<br/>
			<a href="https://www.robinwhittleton.com/">Robin Whittleton</a>,<br/>
			and is based on a transcription produced in 1997 by<br/>
			<b class="name">An Anonymous Volunteer</b> and <b class="name">David Widger</b><br/>
			for<br/>
			<a href="https://www.gutenberg.org/ebooks/965">Project Gutenberg</a><br/>
			and on digital scans available at the<br/>
			<a href="https://archive.org/details/worksofdumas24dumaiala">Internet Archive</a>.</p>

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
			<b>May 11, 2018, 2:13 <abbr class="time eoc">a.m.</abbr></b><br/>
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
					<img alt="The Standard Ebooks logo" src="../images/logo.svg" epub:type="z3998:publisher-logo se:color-depth.black-on-transparent"/>
				</header>
				<p><i epub:type="se:name.publication.book">The Black Tulip</i><br/>
				was published in 1850 by<br/>
				<a href="https://en.wikipedia.org/wiki/Alexandre_Dumas">Alexandre Dumas</a>.<br/>
				It was translated from French in 1902 by<br/>
				<a href="https://en.wikipedia.org/wiki/Peter_F._Collier"><abbr class="name">P. F.</abbr> Collier and Son</a>.</p>
				<p>This ebook was produced for the<br/>
				<a href="https://standardebooks.org">Standard Ebooks project</a><br/>
				by<br/>
				<a href="https://www.robinwhittleton.com/">Robin Whittleton</a>,<br/>
				and is based on a transcription produced in 1997 by<br/>
				<b class="name">An Anonymous Volunteer</b> and <b class="name">David Widger</b><br/>
				for<br/>
				<a href="https://www.gutenberg.org/ebooks/965">Project Gutenberg</a><br/>
				and on digital scans available at the<br/>
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
				<b>May 11, 2018, 2:13 <abbr class="time eoc">a.m.</abbr></b><br/>
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
