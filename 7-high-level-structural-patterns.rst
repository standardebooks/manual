##############################
High Level Structural Patterns
##############################

Section should contain high-level structural patterns for common formatting situations.

Sectioning
**********

#.	The :html:`<body>` element may only have direct children that are :html:`<section>`, :html:`<article>`, or :html:`<nav>`.

#.	Major structural divisions of a larger work, like parts, volumes, books, chapters, or subchapters, are contained in a :html:`<section>` element.

#.	Individual items in a larger collection (like a poem in a poetry collection) are contained in a :html:`<article>` element.

	#.	Collections of very short work, like collections of poems, have all of their content in a single file, and :css:`break-*` CSS is added to generate page breaks between items:

		.. code:: css

			article,
			section{
				break-after: page;
			}

#.	In :html:`<section>` or :html:`<articles>` elements that have titles, the first child element is an :html:`<h1>`–:html:`<h6>` element, an :html:`<hgroup>` element for grouping ordinals, titles, and subtitles, or a :html:`<header>` element containing the section’s title.

Recomposability
===============

“Recomposability” is the concept of generating a single structurally-correct HTML5 file out of an epub file. All Standard Ebooks are recomposable.

#.	XHTML files that contain :html:`<section>` or :html:`<articles>` elements that are semantic children of  :html:`<section>` or :html:`<articles>` elements in other files, are wrapped in stubs of all parent :html:`<section>` or :html:`<articles>` elements, up to the root.

#.	Each such included parent element has the identical :html:`id` and :html:`epub:type` attributes of its real counterpart.

.. class:: no-numbering

Examples
--------

Consider a book that contains several top-level subdivisions: Books 1–4, with each book having 3 parts, and each part having 10 chapters. Below is an example of three files demonstrating the structure necessary to achieve recomposability:

Book 1 (:path:`book-1.xhtml`):

.. code:: html

	<section id="book-1" epub:type="division">
		<h2><span epub:type="label">Book</span> <span epub:type="ordinal z3998:roman">I</span></h2>
	</section>

Book 1, Part 2 (:path:`part-1-2.xhtml`):

.. code:: html

	<section id="book-1" epub:type="division">
		<section id="part-1-2" epub:type="part">
			<h3>
				<span epub:type="label">Part</span>
				<span epub:type="ordinal z3998:roman">II</span>
			</h3>
		</section>
	</section>

Book 1, Part 2, Chapter 3 (:path:`chapter-1-2-3.xhtml`):

.. code:: html

	<section id="book-1" epub:type="division">
		<section id="part-1-2" epub:type="part">
			<section id="chapter-1-2-3" epub:type="chapter">
				<h4>
					<span epub:type="label">Chapter</span>
					<span epub:type="ordinal z3998:roman">III</span>
				</h4>
				<p>...</p>
				<p>...</p>
			</section>
		</section>
	</section>

Headers
*******

#.	:html:`<h1>`–:html:`<h6>` elements are used for headers of sections that are structural divisions of a document, i.e., divisions that appear in the table of contents. :html:`<h1>`–:html:`<h6>` elements *are not* used for headers of components that are not in the table of contents. For example, they are *not* used to mark up the title of a short poem in a chapter, where the poem itself is not a structural component of the larger ebook.

#.	A section containing an :html:`<h1>`–:html:`<h6>` appears in the table of contents.

#.	The book’s title is implicitly at the :html:`<h1>` level, even if :html:`<h1>` is not present in the ebook. An :html:`<h1>` element is only present if the ebook contains a half title page. Because of the implicit :html:`<h1>`, all other sections begin at :html:`<h2>`.

#.	Each :html:`<h1>`–:html:`<h6>` element uses the correct number for the section’s heading level in the overall book, *not* the section’s heading level in the individual file. For example, given an ebook with a file named :path:`part-2.xhtml` containing:

	.. code:: html

		<section id="part-2" epub:type="part">
			<h2><span epub:type="label">Part</span> <span epub:type="ordinal z3998:roman">II</span></h2>
		</section>

	Consider this example for the file :path:`chapter-2-3.xhtml`:

	.. class:: wrong

		.. code:: html

			<section id="part-2" epub:type="part">
				<section id="chapter-2-3" epub:type="chapter">
					<h2 epub:type="ordinal z3998:roman">III</h2>
					...
				</section>
			</section>

	.. class:: corrected

		.. code:: html

			<section id="part-2" epub:type="part">
				<section id="chapter-2-3" epub:type="chapter">
					<h3 epub:type="ordinal z3998:roman">III</h3>
					...
				</section>
			</section>

#.	Each :html:`<h1>`–:html:`<h6>` element has a direct parent :html:`<section>`, :html:`<article>`, :html:`<header>`, or :html:`<hgroup>` element.

#.	:html:`<hgroup>` elements are used to group :html:`<h1>`–:html:`<h6>` elements together when a section’s title has multiple components, for example a header that contains an ordinal and a title, or a header that includes a title and a subtitle.

	#.	:html:`<hgroup>` elements only have :html:`<h1>`–:html:`<h6>` children.

	#.	:html:`<hgroup>` elements are only present if *more than one* :html:`<h1>`–:html:`<h6>` element must be grouped together.

	#.	The first :html:`<h1>`–:html:`<h6>` child of an :html:`<hgroup>` element is the header level for the entire :html:`<hgroup>`. For example, the following :html:`<hgroup>` is at the :html:`<h3>` header level, even though it contains an :html:`<h4>`:

		.. code:: html

			<hgroup>
				<h3 epub:type="ordinal z3998:roman">III</h3>
				<h4 epub:type="title">At the Villa Geneviève</h4>
			</hgroup>

	#.	:html:`<hgroup>` elements in which :html:`<h6>` is the first child have all subsequent children as :html:`<h6>` as well.

#.	Headers follow regular rules for italics, with the exception that headers that are entirely non-English-language are not italicized. Even though they are not italicized, they retain :html:`xml:lang` semantics on the parent element.

	.. code:: html

		<hgroup>
			<h3 epub:type="ordinal z3998:roman">XI</h3>
			<h4 epub:type="title">The <i epub:type="se:name.vessel.ship">Nautilus</i></h4>
		</hgroup>

	.. code:: html

		<hgroup>
			<h3 epub:type="ordinal z3998:roman">XI</h3>
			<h4 epub:type="title" xml:lang="la">Christus Nos Liberavit</h4>
		</hgroup>

	.. code:: html

		<hgroup>
			<h3 epub:type="ordinal z3998:roman">XI</h3>
			<h4 epub:type="title">Miss Thorne’s <i xml:lang="fr">Fête Champêtre</i></h4>
		</hgroup>

#.	If a section does not have any header content, including epigraphs or other non-prose material, then it has :css:`margin-top: 8em;`.

Parts of a section title
========================

Within section titles, we distinguish between labels, ordinals, titles, and subtitles.

#.	Labels are the part of a title that precedes the ordinal. Because they only appear next to ordinals, they are usually wrapped in :html:`<span epub:type="label">` within their parent :html:`<h1>`–:html:`<h6>` element.

	.. code:: html

		<h2><span epub:type="label">Canto</span> <span epub:type="ordinal z3998:roman">III</span></h2>

#.	Ordinals are the number specifying the section’s numeric order in a sequence. They are usually wrapped in :html:`<span epub:type="ordinal">` or :html:`<span epub:type="ordinal z3998:roman">`, if the ordinal is a Roman numeral.

	.. code:: html

		<h2><span epub:type="label">Chapter</span> <span epub:type="ordinal z3998:roman">IV</span></h2>

	Ordinals may also appear without a label:

	.. code:: html

		<h2 epub:type="ordinal z3998:roman">IV</h2>

#.	Labels and ordinals are wrapped in an :html:`<h1>`–:html:`<h6>` element, but that wrapper element is not a semantic title.

#.	Titles are the main title of the section. Often sections may have labels and ordinals, but not titles; or sections may have a title, but no label or ordinal.

	.. code:: html

		<h2 epub:type="title">The New Villa</h2>

	.. code:: html

		<hgroup>
			<h2 epub:type="ordinal z3998:roman">IV</h2>
			<h3 epub:type="title">The Letter Signed “Bella”</h3>
		</hgroup>

#.	Subtitles are supplementary titles in addition to the main title.

	.. code:: html

		<hgroup>
			<h2 epub:type="title">Between the Scenes</h2>
			<h3 epub:type="subtitle">Progress of the Story Through the Post</h3>
		</hgroup>

Header patterns
===============

#.	Sections with ordinals but without titles:

	.. code:: html

		<h2 epub:type="ordinal z3998:roman">XI</h2>

#.	Sections with titles but without ordinals:

	.. code:: html

		<h2 epub:type="title">A Daughter of Albion</h2>

#.	Sections with titles and ordinals:

	.. code:: html

		<hgroup>
			<h2 epub:type="ordinal z3998:roman">XI</h2>
			<h3 epub:type="title">Who Stole the Tarts?</h3>
		</hgroup>

#.	Sections titles and subtitles but no ordinals:

	.. code:: html

		<hgroup>
			<h2 epub:type="title">An Adventure</h2>
			<h3 epub:type="subtitle">(A Driver’s Story)</h3>
		</hgroup>

#.	Sections with labels and ordinals:

	.. code:: html

		<h2>
			<span epub:type="label">Book</span>
			<span epub:type="ordinal z3998:roman">II</span>
		</h2>

#.	Sections with labels, ordinals, and titles:

	.. code:: html

		<hgroup>
			<h2>
				<span epub:type="label">Book</span>
				<span epub:type="ordinal z3998:roman">II</span>
			</h2>
			<h3 epub:type="title">The Man in the Street</h3>
		</hgroup>

#.	Sections that have a non-unique title, but that are required to be identifed in the ToC with a unique title (e.g., multiple poems identified as “Sonnet” in the body matter, which require their ToC entry to contain the poem’s first line to differentiate them):

	.. code:: html

		<hgroup>
			<h2 epub:type="title">Sonnet</h2>
			<h3 hidden="hidden" epub:type="subtitle">Happy Is England!</h3>
		</hgroup>

#.	Sections that require titles, but that are not in the table of contents:

	.. code:: css

		header{
			font-variant: small-caps;
			margin: 1em;
			text-align: center;
		}

	.. code:: html

		<header>
			<p>The Title of a Short Poem</p>
		</header>

#.	Sections without any titles at all have :css:`margin-top: 20vh` applied to their sectioning container.

	.. code:: css

		section[epub|type~="preface"]{
			margin-top: 20vh;
		}

	.. code:: html

		<section epub:type="preface">
			<p>Being observations or memorials of the most remarkable occurrences...</p>
			<p>...</p>
		</section>

#.	Half title pages without subtitles:

	.. code:: html

		<h1 epub:type="fulltitle">Eugene Onegin</h1>


#.	Half title pages with subtitles:

	.. code:: html

		<hgroup epub:type="fulltitle">
			<h1 epub:type="title">His Last Bow</h1>
			<h2 epub:type="subtitle">Some Reminiscences of Sherlock Holmes</h2>
		</hgroup>

Bridgeheads
===========

Bridgeheads are sections in a chapter header that give an abstract or summary of the following chapter. They may be in prose or in a short list with clauses separated by em dashes.

#.	The last clause in a bridgehead ends in appropriate punctuation, like a period.

#.	Bridgeheads have the following CSS and HTML structure:

	.. code:: css

		[epub|type~="bridgehead"]{
			display: inline-block;
			font-style: italic;
			max-width: 60%;
			text-align: justify;
			text-indent: 0;
		}

		[epub|type~="bridgehead"] i{
			font-style: normal;
		}

		[epub|type~="z3998:poem"] [epub|type~="bridgehead"],
		[epub|type~="z3998:verse"] [epub|type~="bridgehead"],
		[epub|type~="z3998:song"] [epub|type~="bridgehead"],
		[epub|type~="z3998:hymn"] [epub|type~="bridgehead"]{
			text-align: justify;
		}

	.. code:: html

		<header>
			<h2 epub:type="ordinal z3998:roman">I</h2>
			<p epub:type="bridgehead">Which treats of the character and pursuits of the famous gentleman Don Quixote of La Mancha.</p>
		</header>

	.. code:: html

		<header>
			<h2 epub:type="ordinal z3998:roman">X</h2>
			<p epub:type="bridgehead">Our first night⁠:ws:`wj`—Under canvas⁠:ws:`wj`—An appeal for help⁠:ws:`wj`—Contrariness of teakettles, how to overcome⁠:ws:`wj`—Supper⁠:ws:`wj`—How to feel virtuous⁠:ws:`wj`—Wanted! a comfortably-appointed, well-drained desert island, neighbourhood of South Pacific Ocean preferred⁠:ws:`wj`—Funny thing that happened to George’s father⁠:ws:`wj`—A restless night.</p>
		</header>

#.	Bridgeheads are typically set in italics. `Exceptions are allowed according to rules for italics </manual/VERSION/8-typography#8.2.13>`__.

Dedications
***********

#.	Dedications are typically full-page, centered on the page for ereaders that support advanced CSS. For all other ereaders, the dedication is horizontally centered with a small margin above it.

#.	All dedications include this base CSS:

	.. code:: css

		/* All dedications */
		section[epub|type~="dedication"]{
			text-align: center;
		}

		section[epub|type~="dedication"] > *{
			display: inline-block;
			margin: auto;
			margin-top: 3em;
			max-width: 80%;
		}

		@supports(display: flex){
			section[epub|type~="dedication"]{
				align-items: center;
				box-sizing: border-box;
				display: flex;
				flex-direction: column;
				justify-content: center;
				min-height: calc(98vh - 3em);
				padding-top: 3em;
			}

			section[epub|type~="dedication"] > *{
				margin: 0;
			}
		}
		/* End all dedications */

#.	Dedications are frequently styled uniquely by the authors. Therefore Standard Ebooks producers have freedom to style dedications to match page scans, for example by including small caps, different font sizes, alignments, etc.

Epigraphs
*********

#.	All epigraphs include this CSS:

	.. code:: css

		/* All epigraphs */
		[epub|type~="epigraph"]{
			font-style: italic;
			hyphens: none;
			-epub-hyphens: none;
		}

		[epub|type~="epigraph"] em,
		[epub|type~="epigraph"] i{
			font-style: normal;
		}

		[epub|type~="epigraph"] cite{
			margin-top: 1em;
			font-style: normal;
			font-variant: small-caps;
		}

		[epub|type~="epigraph"] cite i{
			font-style: italic;
		}
		/* End all epigraphs */

#.	Epigraphs are typically set in italics. `Exceptions are allowed according to rules for italics </manual/VERSION/8-typography#8.2.13>`__.

#.	Epigraphs may sometimes contain quotes from plays and drama. Such quotations use the `standard play formatting  </manual/VERSION/7-high-level-structural-patterns#7.6>`__ and this additional CSS to remove italics from personas:

	.. code:: css

		[epub|type~="epigraph"] [epub|type~="z3998:persona"]{
			font-style: normal;
		}

Epigraphs in section headers
============================

#.	Epigraphs in section headers have the quote source in a :html:`<cite>` element set in small caps, without a leading em-dash and without a trailing period.

	.. class:: wrong

		.. code:: html

			<header>
				<h2 epub:type="ordinal z3998:roman">II</h2>
				<blockquote epub:type="epigraph">
					<p>“Desire no more than to thy lot may fall. …”</p>
					<cite>—Chaucer.</cite>
				</blockquote>
			</header>

	.. class:: corrected

		.. code:: css

			header [epub|type~="epigraph"] cite{
				font-variant: small-caps;
			}

		.. code:: html

			<header>
				<h2 epub:type="ordinal z3998:roman">II</h2>
				<blockquote epub:type="epigraph">
					<p>“Desire no more than to thy lot may fall. …”</p>
					<cite>Chaucer</cite>
				</blockquote>
			</header>

#.	In addition to the `CSS used for all epigraphs </manual/VERSION/7-high-level-structural-patterns#7.3.1>`__, this additional CSS is included for epigraphs in section headers:

	.. code:: css

		/* Epigraphs in section headers */
		article > header [epub|type~="epigraph"],
		section > header [epub|type~="epigraph"]{
			display: inline-block;
			margin: auto;
			max-width: 80%;
			text-align: initial;
		}

		article > header [epub|type~="epigraph"] + *,
		section > header [epub|type~="epigraph"] + *{
			margin-top: 3em;
		}

		@supports(display: table){
			article > header [epub|type~="epigraph"],
			section > header [epub|type~="epigraph"]{
				display: table;
			}
		}
		/* End epigraphs in section headers */

Full-page epigraphs
===================

#.	In full-page epigraphs, the epigraph is centered on the page for ereaders that support advanced CSS. For all other ereaders, the epigraph is horizontally centered with a small margin above it.

#.	Full-page epigraphs that contain multiple quotations are represented by multiple :html:`<blockquote>` elements.

#.	In addition to the `CSS used for all epigraphs </manual/VERSION/7-high-level-structural-patterns#7.3.1>`__, this additional CSS is included for full-page epigraphs:

	.. code:: css

		/* Full-page epigraphs */
		section[epub|type~="epigraph"]{
			text-align: center;
		}

		section[epub|type~="epigraph"] > *{
			display: inline-block;
			margin: auto;
			margin-top: 3em;
			max-width: 80%;
			text-align: initial;
		}

		@supports(display: flex){
			section[epub|type~="epigraph"]{
				align-items: center;
				box-sizing: border-box;
				display: flex;
				flex-direction: column;
				justify-content: center;
				min-height: calc(98vh - 3em);
				padding-top: 3em;
			}

			section[epub|type~="epigraph"] > *{
				margin: 0;
			}

			section[epub|type~="epigraph"] > * + *{
				margin-top: 3em;
			}
		}
		/* End full-page epigraphs */

#.	Example HTML:

	.. code:: html

		<body epub:type="frontmatter">
			<section id="epigraph" epub:type="epigraph">
				<blockquote>
					<p>Reorganisation, irrespectively of God or king, by the worship of Humanity, systematically adopted.</p>
					<p>Man’s only right is to do his duty.</p>
					<p>The Intellect should always be the servant of the Heart, and should never be its slave.</p>
				</blockquote>
				<blockquote>
					<p>“We tire of thinking and even of acting; we never tire of loving.”</p>
				</blockquote>
			</section>
		</body>

Poetry, verse, and songs
************************

Unfortunately there’s no great way to semantically format poetry in HTML. As such, unrelated elements are conscripted for use in poetry.

#.	A stanza is represented by a :html:`<p>` element styled with this CSS:

	.. code:: css

		[epub|type~="z3998:poem"] p{
			text-align: initial;
			text-indent: 0;
		}

		[epub|type~="z3998:poem"] p + p{
			margin-top: 1em;
		}

#.	Each stanza contains :html:`<span>` elements, each one representing a line in the stanza, styled with this CSS:

	.. code:: css

		[epub|type~="z3998:poem"] p > span{
			display: block;
			padding-left: 1em;
			text-indent: -1em;
		}

#.	Each :html:`<span>` line is followed by a :html:`<br/>` element, except for the last line in a stanza, styled with this CSS:

	.. code:: css

		[epub|type~="z3998:poem"] p > span + br{
			display: none;
		}

#.	Indented :html:`<span>` lines have the :value:`i1` class. :italics:`Do not` use :ws:`nbsp` for indentation. Indenting to different levels is done by incrementing the class to :css:`i2`, :css:`i3`, and so on, and including the appropriate CSS.

	.. code:: css

		p span.i1{
			padding-left: 2em;
			text-indent: -1em;
		}

		p span.i2{
			padding-left: 3em;
			text-indent: -1em;
		}

#.	Poems, songs, and verse that are shorter part of a longer work, like a novel, are wrapped in a :html:`<blockquote>` element.

	.. code:: html

		<blockquote epub:type="z3998:poem">
			<p>
				<span>...</span>
				<br/>
				<span>...</span>
			</p>
		</blockquote>

#.	The parent element of poetry, verse, or song, has the semantic inflection of :value:`z3998:poem`, :value:`z3998:verse`, :value:`z3998:song`, or :value:`z3998:hymn`.

	#.	The z3998 vocabulary does not explicitly define their terms for each of the above; these are the standards for our productions.

		#.	:value:`z3998:poem` is used when an entire poem is quoted, even a short one.

		#.	:value:`z3998:verse` is used for poem or verse fragments.

		#.	:value:`z3998:song` is used when song lyrics are quoted, in whole or in part.

		#.	:value:`z3998:hymn` is used when the song lyrics are for a hymn, either well known (e.g. “Amazing Grace”) or specifically labeled as such in the source text. When in doubt, use :value:`z3998:song`.

#.	If a poem is quoted and has one or more lines removed, the removed lines are represented with a vertical ellipses (:utf:`⋮` or U+22EE) in a :html:`<span class="elision">` element styled with this CSS:

	.. code:: css

		span.elision{
			margin: .5em;
			margin-left: 3em;
		}

		/* If eliding within an epigraph, include this additional style: */
		[epub|type~="epigraph"] span.elision{
			font-style: normal;
		}

	.. code:: html

		<blockquote epub:type="z3998:verse">
			<p>
				<span>O Lady! we receive but what we give,</span>
				<br/>
				<span>And in our life alone does nature live:</span>
				<br/>
				<span>Ours is her wedding garments, ours her shroud!</span>
				<br/>
				<span class="elision">⋮</span>
				<br/>
				<span class="i1">Ah! from the soul itself must issue forth</span>
				<br/>
				<span>A light, a glory, a fair luminous cloud,</span>
			</p>
		</blockquote>

.. class:: no-numbering

Examples
========

Note that below we include CSS for the :css:`.i2` class, even though it’s not used in the example. It’s included to demonstrate how to adjust the CSS for indentation levels after the first.

.. code:: css

	[epub|type~="z3998:poem"] p{
		text-align: initial;
		text-indent: 0;
	}

	[epub|type~="z3998:poem"] p > span{
		display: block;
		padding-left: 1em;
		text-indent: -1em;
	}

	[epub|type~="z3998:poem"] p > span + br{
		display: none;
	}

	[epub|type~="z3998:poem"] p + p{
		margin-top: 1em;
	}

	p span.i1{
		padding-left: 2em;
		text-indent: -1em;
	}

	p span.i2{
		padding-left: 3em;
		text-indent: -1em;
	}

.. code:: html

	<blockquote epub:type="z3998:poem">
		<p>
			<span>“How doth the little crocodile</span>
			<br/>
			<span class="i1">Improve his shining tail,</span>
			<br/>
			<span>And pour the waters of the Nile</span>
			<br/>
			<span class="i1">On every golden scale!</span>
		</p>
		<p>
			<span>“How cheerfully he seems to grin,</span>
			<br/>
			<span class="i1">How neatly spread his claws,</span>
			<br/>
			<span>And welcome little fishes in</span>
			<br/>
			<span class="i1"><em>With gently smiling jaws!</em>”</span>
		</p>
	</blockquote>

Plays and drama
***************

#.	Dialog in plays is structured using :html:`<table>` elements.

#.	Each :html:`<tr>` is either a block of dialog or a standalone stage direction.

#.	Personas are typically characters that have speaking roles. They are set in small caps and never in italics, even if the surrounding text is in italics.

#.	Works that are plays or that contain sections of dramatic dialog have this core CSS:

	.. code:: css

		[epub|type~="z3998:drama"] table,
		table[epub|type~="z3998:drama"]{
			border-collapse: collapse;
			margin: 1em auto;
			width: 100%;
		}

		[epub|type~="z3998:drama"] tr:first-child td{
			padding-top: 0;
		}

		[epub|type~="z3998:drama"] tr:last-child td{
			padding-bottom: 0;
		}

		[epub|type~="z3998:drama"] td{
			vertical-align: top;
			padding: .5em;
		}

		[epub|type~="z3998:drama"] td:last-child{
			padding-right: 0;
		}

		[epub|type~="z3998:drama"] td:first-child{
			padding-left: 0;
		}

		[epub|type~="z3998:drama"] td[epub|type~="z3998:persona"]{
			hyphens: none;
			-epub-hyphens: none;
			text-align: right;
			width: 20%;
		}

		[epub|type~="z3998:stage-direction"]{
			font-style: italic;
		}

		[epub|type~="z3998:stage-direction"] [epub|type~="z3998:persona"],
		em [epub|type~="z3998:persona"],
		i [epub|type~="z3998:persona"]{
			font-style: normal;
		}

		[epub|type~="z3998:stage-direction"]::before{
			content: "(";
			font-style: normal;
		}

		[epub|type~="z3998:stage-direction"]::after{
			content: ")";
			font-style: normal;
		}

		[epub|type~="z3998:persona"]{
			font-variant: all-small-caps;
		}

		section[epub|type~="z3998:scene"] > p{
			margin: 1em auto;
			width: 75%;
		}

Dialog rows
===========

#.	The first child of a row of dialog is a :html:`<td>` element with the semantic inflection of :value:`z3998:persona`.

#.	The second child of a row of dialog is a :html:`<td>` element containing the actual dialog. Elements that contain only one line of dialog do not have a block-level child (like :html:`<p>`).

	.. code:: html

		<tr>
			<td epub:type="z3998:persona">Algernon</td>
			<td>Did you hear what I was playing, Lane?</td>
		</tr>
		<tr>
			<td epub:type="z3998:persona">Lane</td>
			<td>I didn’t think it polite to listen, sir.</td>
		</tr>

	#.	Dialog rows that have dialog broken over several lines, i.e. in dialog in verse form, have `semantics, structure, and CSS for verse. </manual/VERSION/7-high-level-structural-patterns#7.5>`__ The :html:`<td>` element has the :value:`z3998:verse` semantic.

		.. code:: html

			<tr>
				<td epub:type="z3998:persona">Queen Isabel</td>
				<td epub:type="z3998:verse">
					<p>
						<span>Our gracious brother, I will go with them.</span>
						<br/>
						<span>Haply a woman’s voice may do some good,</span>
						<br/>
						<span>When articles too nicely urg’d be stood on.</span>
					</p>
				</td>
			</tr>

#.	When several personas speak at once, or a group of personas (“The Actors”) speaks at once, the containing :html:`<tr>` element has the :value:`together` class, and the first :html:`<td>` child has a :html:`rowspan` attribute corresponding to the number of lines spoken together.

	.. code:: css

		tr.together{
			break-inside: avoid;
		}

		tr.together td{
			padding: 0 .5em 0 0;
			vertical-align: middle;
		}

		tr.together td:only-child,
		tr.together td + td{
			border-left: 1px solid;
		}

		.together + .together td[rowspan],
		.together + .together td[rowspan] + td{
			padding-top: .5em;
		}

		[epub|type~="z3998:drama"] .together td:last-child{
			padding-left: .5em;
		}

	.. code:: html

		<tr class="together">
			<td rowspan="3" epub:type="z3998:persona">The Actors</td>
			<td>Oh, what d’you think of that?</td>
		</tr>
		<tr class="together">
			<td>Only the mantle?</td>
		</tr>
		<tr class="together">
			<td>He must be mad.</td>
		</tr>
		<tr class="together">
			<td rowspan="2" epub:type="z3998:persona">Some Actresses</td>
			<td>But why?</td>
		</tr>
		<tr class="together">
			<td>Mantles as well?</td>
		</tr>

Stage direction
===============

#.	Stage direction is wrapped in an :html:`<i epub:type="z3998:stage-direction">` element.

	#.	Stage directions that are included from a different edition additionally have the :html:`class="editorial"` attribute, with this additional CSS:

		.. code:: css

			[epub|type~="z3998:stage-direction"].editorial::before{
				content: "[";
			}

			[epub|type~="z3998:stage-direction"].editorial::after{
				content: "]";
			}

#.	Personas mentioned in stage direction are wrapped in a :html:`<b epub:type="z3998:persona">` element.

	#.	Possessive :string:`’s` or :string:`’` are included within the associated :html:`<b>` element.

		.. code:: html

			<i epub:type="z3998:stage-direction">Lowering his voice for <b epub:type="z3998:persona">Maury’s</b> ear alone.</i>

#.	Stage direction in shorthand (for example, :string:`Large French window, R. 3 E.`) is wrapped in an :html:`<abbr epub:type="z3998:stage-direction">` element, with this additional CSS:

	.. code:: css

		abbr[epub|type~="z3998:stage-direction"]{
			font-style: normal;
			font-variant: all-small-caps;
		}

		abbr[epub|type~="z3998:stage-direction"]::before,
		abbr[epub|type~="z3998:stage-direction"]::after{
			content: '';
		}

Stage direction rows
--------------------

#.	The first child of a row containing only stage direction is an empty :html:`<td>` element.

#.	The second child of a row containing only stage direction is a :html:`<td>` element containing the stage direction.

.. class:: no-numbering

Examples
~~~~~~~~

.. code:: html

	<tr>
		<td/>
		<td>
			<i epub:type="z3998:stage-direction">Large French window, <abbr epub:type="z3998:stage-direction" class="eoc">R. 3 E.</abbr> <b epub:type="z3998:persona">Lane</b> is arranging afternoon tea on the table, and after the music has ceased, <b epub:type="z3998:persona">Algernon</b> enters.</i>
		</td>
	</tr>

Inline stage direction
----------------------

#.	Inline stage direction that is not an interjection within a containing clause begins with a capital letter and ends in punctuation, usually a period.

#.	Inline stage direction that *is* an interjection within a containing clause does not begin with a capital letter, and ending punctuation is optional and usually omitted.

.. class:: no-numbering

Examples
~~~~~~~~

.. code:: html

	<tr>
		<td epub:type="z3998:persona">Jackson</td>
		<td>I see you don’t know much! A costume <i epub:type="z3998:stage-direction">putting his finger on his forehead</i> is a thing which calls for deep thought. Have you seen my Sun here? <i epub:type="z3998:stage-direction">Strikes his posterior.</i> I looked for it two years.</td>
	</tr>

Works that are complete plays
=============================

#.	The top-level element (usually :html:`<body>`) has the :value:`z3998:drama` semantic inflection.

#.	Acts are :html:`<section>` elements containing at least one :html:`<table>` for dialog, and optionally containing an act title and other top-level stage direction.

#.	Introductory or high-level stage direction is presented using :html:`<p>` elements outside of the dialog table.

	.. code:: html

		<body epub:type="bodymatter z3998:fiction z3998:drama">
			<section id="act-1" epub:type="chapter z3998:scene">
				<h2><span epub:type="label">Act</span> <span epub:type="ordinal z3998:roman">I</span></h2>
				<p>Scene: Morning-room in Algernon’s flat in Half-Moon Street. The room is luxuriously and artistically furnished. The sound of a piano is heard in the adjoining room.</p>
				<table>
					...
				</table>
				<p epub:type="z3998:stage-direction">Act Drop</p>
			</section>
		</body>

#.	Dramatis personae are presented as a :html:`<ul>` element listing the characters.

	.. code:: css

		[epub|type~="z3998:dramatis-personae"]{
			text-align: center;
		}

		[epub|type~="z3998:dramatis-personae"] p{
			text-indent: 0;
		}

		[epub|type~="z3998:dramatis-personae"] ul{
			list-style: none;
			margin: 0;
			padding: 0;
		}

		[epub|type~="z3998:dramatis-personae"] ul li{
			margin: 1em;
			font-style: italic;
		}

		[epub|type~="z3998:dramatis-personae"] ul + p{
			margin-top: 2em;
		}

	.. code:: html

		<section id="dramatis-personae" epub:type="z3998:dramatis-personae">
			<h2 epub:type="title">Dramatis Personae</h2>
			<ul>
				<li>
					<p>King Henry <span epub:type="z3998:roman">V</span></p>
				</li>
				<li>
					<p>Duke of Clarence, brother to the King</p>
				</li>
				...
			</ul>
		</section>

Letters
*******

Letters require particular attention to styling and semantic inflection. Letters may not exactly match the formatting in the source scans, but they are in visual sympathy with the source.

#.	Letters are wrapped in a :html:`<blockquote>` element with the appropriate semantic inflection, usually :value:`z3998:letter`.

Letter headers
==============

#.	Parts of a letter prior to the body of the letter, for example the location where it is written, the date, and the salutation, are wrapped in a :html:`<header>` element.

#.	 If there is only a salutation and no other header content, the :html:`<header>` element is omitted.

#.	The location and date of a letter have the semantic inflection of :value:`se:letter.dateline`. Dates are in a :html:`<time>` element with a computer-readable date.

	.. code:: html

		<header>
			<p epub:type="se:letter.dateline">Blarney Castle, <time datetime="1863-10-11">11th of October, 1863</time></p>
		</header>

#.	The salutation (for example, “Dear Sir” or “My dearest Jane”) has the semantic inflection of :value:`z3998:salutation`.

#.	The first line of a letter after the salutation is not indented.

#.	Salutations that are within the first line of the letter are wrapped in a :html:`<span epub:type="z3998:salutation">` element (or a :html:`<b epub:type="z3998:salutation">` element if small-caps are desired).

	.. code:: html

		<p><b epub:type="z3998:salutation">Dear Mother</b>, I was so happy to hear from you.</p>

#.	The name of the recipient of the letter, when set out other than within a saluation (for example a letter headed “To: John Smith Esquire”), is given the semantic inflection of :value:`z3998:recipient`. Sometimes this may occur at the end of a letter, particularly for more formal communications, in which case it is placed within a :html:`<footer>` element.

Letter footers
==============

#.	Parts of a letter after the body of the letter, for example the signature or postscript, are wrapped in a :html:`<footer>` element.

#.	The :html:`<footer>` element has the following CSS:

	.. code:: css

		footer{
			margin-top: 1em;
			text-align: right;
		}

#.	The valediction (for example, “Yours Truly” or “With best regards”) has the semantic inflection of :value:`z3998:valediction`.

#.	The sender’s name has semantic inflection of :value:`z3998:sender`. If the name appears to be a signature to the letter, it has the :value:`z3998:signature` semantic inflection and corresponding CSS.

	.. code:: css

		[epub|type~="z3998:signature"]{
			font-variant: small-caps;
		}

	.. code:: html

		<footer>
			<p epub:type="z3998:sender z3998:signature"><abbr class="name">R. A.</abbr> Johnson</p>
		</footer>

	.. code:: html

		<footer>
			<p epub:type="z3998:sender"><span epub:type="z3998:signature">John Doe</span>, President</p>
		</footer>

#.	Postscripts have the semantic inflection of :value:`z3998:postscript` and the following CSS:

	.. code:: css

		[epub|type~="z3998:postscript"]{
			margin-top: 1em;
			text-align: initial;
			text-indent: 0;
		}

	#.	Postscripts that contain multiple paragraphs are grouped by having their contents wrapped in :html:`<div epub:type="z3998:postscript">`.

.. class:: no-numbering

Examples
========

.. code:: css

	[epub|type~="z3998:letter"] header{
  		text-align: right;
	}

	footer{
		margin-top: 1em;
		text-align: right;
	}

	[epub|type~="z3998:salutation"] + p,
	[epub|type~="z3998:letter"] header + p{
		text-indent: 0;
	}

	[epub|type~="z3998:sender"],
	[epub|type~="z3998:recipient"],
	[epub|type~="z3998:salutation"],
	[epub|type~="z3998:signature"]{
		font-variant: small-caps;
	}

	[epub|type~="z3998:postscript"]{
		margin-top: 1em;
		text-align: initial;
		text-indent: 0;
	}

.. code:: html

	<blockquote epub:type="z3998:letter">
		<p epub:type="z3998:salutation">Dearest Auntie,</p>
		<p>Please may we have some things for a picnic? Gerald will bring them. I would come myself, but I am a little tired. I think I have been growing rather fast.</p>
		<footer>
			<p epub:type="z3998:valediction">Your loving niece,</p>
			<p epub:type="z3998:sender z3998:signature">Mabel</p>
			<p epub:type="z3998:postscript"><abbr class="initialism">P.S.</abbr>:ws:`wj`—Lots, please, because some of us are very hungry.</p>
		</footer>
	</blockquote>

.. code:: html

	<blockquote epub:type="z3998:letter">
		<header>
			<p epub:type="se:letter.dateline">Gracechurch-street, <time datetime="08-02">August 2</time>.</p>
		</header>
		<p><span epub:type="z3998:salutation">My dear Brother</span>, At last I am able to send you some tidings of my niece, and such as, upon the whole, I hope will give you satisfaction. Soon after you left me on Saturday, I was fortunate enough to find out in what part of London they were. The particulars, I reserve till we meet. It is enough to know they are discovered, I have seen them both⁠:ws:`wj`—</p>
		<p>I shall write again as soon as anything more is determined on.</p>
		<footer>
			<p epub:type="z3998:valediction">Yours, etc.</p>
			<p epub:type="z3998:sender z3998:signature">Edward Gardner</p>
		</footer>
	</blockquote>

Images
******

#.	Each image has a unique :html:`id` attribute.

	#.	That attribute's name is :value:`illustration-` followed by :value:`-N`, where :value:`N` is the sequence number of the element starting at :value:`1`.

	#.	If the image is inline with the text, the :html:`id` attribute is on the :html:`<img>` element.

			.. code:: html

				<img alt="..." src="..." id="illustration-1" />

	#.	When contained in a :html:`<figure>` element, the :html:`<img>` element does not have an :html:`id` attribute; instead the :html:`<figure>` element has the :html:`id` attribute.

			.. code:: html

				<figure id="illustration-3">
					<img alt="..." src="..." />

#.	:html:`<img>` elements have an :html:`alt` attribute that uses prose to describe the image in detail; this is what screen reading software will read aloud.

	#.	The :html:`alt` attribute describes the visual image itself in words, which is not the same as writing a caption or describing its place in the book.

		.. class:: wrong

			.. code:: html

				<img alt="The illustration for chapter 10" src="..." />

		.. class:: wrong

			.. code:: html

				<img alt="Pierre’s fruit-filled dinner" src="..." />

		.. class:: corrected

			.. code:: html

				<img alt="An apple and a pear inside a bowl, resting on a table." src="..." />

		#.	The :html:`alt` attribute does not contain no-break spaces or word joiners.

	#.	The :html:`alt` attribute is one or more complete sentences ended with periods or other appropriate punctuation. It is not composed of sentence fragments or complete sentences without ending punctuation.

	#.	The :html:`alt` attribute is not necessarily the same as text in the image’s sibling :html:`<figcaption>` element, if one is present.

#.	:html:`<img>` elements have semantic inflection denoting the type of image. Common values are :value:`z3998:illustration` or :value:`z3998:photograph`.

#.	:html:`<img>` element whose image is black-on-white line art (i.e. exactly two colors, **not** grayscale!) are PNG files with a transparent background. They have the :value:`se:image.color-depth.black-on-transparent` semantic inflection.

#.	:html:`<img>` elements that are meant to be aligned on the block level or displayed as full-page images are contained in a parent :html:`<figure>` element, with an optional :html:`<figcaption>` sibling.

	#.	An optional :html:`<figcaption>` element containing  a concise context-dependent caption may follow the :html:`<img>` element within a :html:`<figure>` element. This caption depends on the surrounding context, and is not necessarily (or even ideally) identical to the :html:`<img>` element’s :html:`alt` attribute.

	#.	All figure elements, regardless of positioning, have this CSS:

		.. code:: css

			figure img{
				display: block;
				margin: auto;
				max-width: 100%;
			}

			figcaption{
				font-size: .75em;
				font-style: italic;
				margin: 1em;
			}

			figcaption p + p{
				text-indent: 0;
			}

	#.	:html:`<figure>` elements that are meant to be displayed as full-page images have the :value:`full-page` class and this additional CSS:

		.. code:: css

			figure.full-page{
				break-after: page;
				break-before: page;
				break-inside: avoid;
				margin: 0;
				max-height: 100%;
				text-align: center;
			}

			@supports(display: flex) and (max-height: 100vh){
				figure.full-page{
					display: flex;
					flex-direction: column;
					max-height: 100vh;
				}

				figure.full-page img{
					height: 100%;
				}
			}

	#.	:html:`<figure>` elements that meant to be aligned block-level with the text have this additional CSS:

		.. code:: css

			figure{
				margin: 1em auto;
				text-align: center;
			}

.. class:: no-numbering

Examples
========

.. code:: css

	/* If the image is meant to be on its own page, use this selector... */
	figure.full-page{
		margin: 0;
		max-height: 100%;
		break-before: page;
		break-after: page;
		break-inside: avoid;
		text-align: center;
	}

	/* If the image is meant to be inline with the text, use this selector... */
	figure{
		margin: 1em auto;
		text-align: center;
	}

	/* In all cases, also include the below styles */
	figure img{
		display: block;
		margin: auto;
		max-width: 100%;
	}

	figcaption{
		font-size: .75em;
		font-style: italic;
		margin: 1em;
	}

.. code:: html

	<p>...</p>
	<figure id="illustration-10">
		<img alt="An apple and a pear inside a bowl, resting on a table." src="../images/illustration-10.jpg" epub:type="z3998:photograph"/>
		<figcaption>The Monk’s Repast</figcaption>
	</figure>

.. code:: html

	<p>...</p>
	<figure class="full-page" id="image-11">
		<img alt="A massive whale breaching the water, with a sailor floating in the water directly within the whale’s mouth." src="../images/illustration-11.jpg" epub:type="z3998:illustration"/>
		<figcaption>The Whale eats Sailor Jim.</figcaption>
	</figure>

.. code:: html

	<p>He saw strange alien text that looked like this: <img alt="A line of alien heiroglyphs." src="../images/alien-text.svg" epub:type="z3998:illustration se:color-depth.black-on-transparent" />. There was nothing else amongst the ruins.</p>

List of Illustrations (the LoI)
*******************************

If an ebook has any illustrations that are *major structural components* of the work (even just one!), then the ebook includes an :path:`loi.xhtml` file at the end of the ebook. This file lists the illustrations in the ebook, along with a short caption or description.

#.	The LoI is an XHTML file named :path:`./src/epub/text/loi.xhtml`.

#.	The LoI file has the :value:`backmatter` semantic inflection.

#.	The LoI only contains links to images that are major structural components of the work.

	#.	An illustration is a major structural component if, for example: it is an illustration of events in the book, like a full-page drawing or end-of-chapter decoration; it is essential to the plot, like a diagram of a murder scene or a map; or it is a component of the text, like photographs in a documentary narrative.

	#.	An illustration is *not* a major structural components if, for example: it is a drawing used to represent a person’s signature, like an X mark; it is an inline drawing representing text in alien languages; it is a drawing used as a layout element to illustrate forms, tables, or diagrams.

#.	The LoI file contains a single :html:`<section id="loi" epub:type="loi">` element, which in turn contains a :html:`<nav epub:type="loi">` element, which in turn contains an :html:`<h2 epub:type="title">List of Illustrations</h2>` element, followed by an :html:`<ol>` element, which in turn contains list items representing the images.

#.	If an image listed in the LoI has a :html:`<figcaption>` element, then that caption is used in the anchor text for that LoI entry. If not, the image’s :html:`alt` attribute is used. If the :html:`<figcaption>` element is too long for a concise LoI entry, the :html:`alt` attribute is used instead.

#.	Links to the images go directly to the image’s corresponding :html:`id` hashes, not just the top of the containing file.

.. class:: no-numbering

Examples
========

.. code:: html

	<?xml version="1.0" encoding="utf-8"?>
	<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" epub:prefix="z3998: http://www.daisy.org/z3998/2012/vocab/structure/, se: https://standardebooks.org/vocab/1.0" xml:lang="en-GB">
		<head>
			<title>List of Illustrations</title>
			<link href="../css/core.css" rel="stylesheet" type="text/css"/>
			<link href="../css/local.css" rel="stylesheet" type="text/css"/>
		</head>
		<body epub:type="backmatter">
			<section id="loi" epub:type="loi">
				<nav epub:type="loi">
					<h2 epub:type="title">List of Illustrations</h2>
					<ol>
						<li>
							<p>
								<a href="preface.xhtml#the-edge-of-the-world">The Edge of the World</a>
							</p>
						</li>
						...
					</ol>
				</nav>
			</section>
		</body>
	</html>

Endnotes
********

#.	Ebooks do not have footnotes, only endnotes. Footnotes are instead converted to endnotes.

#.	:string:`Ibid.` is a Latinism commonly used in endnotes to indicate that the source for a quotation or reference is the same as the last-mentioned source.

	When the last-mentioned source is in the previous endnote, :string:`Ibid.` is replaced by the full reference; otherwise :string:`Ibid.` is left as-is. Since ebooks use popup endnotes, :string:`Ibid.` becomes meaningless without context.

Noterefs
========

The noteref is the superscripted number in the body text that links to the endnote at the end of the book.

#.	Endnotes are referenced in the text by an :html:`<a>` element with the semantic inflection :value:`noteref`.

	#.	Noterefs point directly to the corresponding endnote :html:`<li>` element in the endnotes file.

	#.	Noterefs have an :html:`id` attribute like :value:`noteref-n`, where :value:`n` is identical to the endnote number.

	#.	The text of the noteref is the endnote number.

#.	If located at the end of a sentence, noterefs are placed after ending punctuation.

#.	If the endnote references an entire sentence in quotation marks, or the last word in a sentence in quotation marks, then the noteref is placed outside the quotation marks.

The endnotes file
=================

#.	Endnotes are in an XHTML file named :path:`./src/epub/text/endnotes.xhtml`.

#.	The endnotes file has the :value:`backmatter` semantic inflection.

#.	The endnotes file contains a single :html:`<section id="endnotes" epub:type="endnotes">` element, which in turn contains an :html:`<h2 epub:type="title">Endnotes</h2>` element, followed by an :html:`<ol>` element containing list items representing the endnotes.

#.	Each endnote’s :html:`id` attribute is in sequential ascending order.

Individual endnotes
===================

#.	An endnote is an :html:`<li id="note-n" epub:type="endnote">` element containing one or more block-level text elements and one backlink element.

#.	Each endnote’s contains a backlink, which has the semantic inflection :value:`backlink`, contains the text :string:`↩`, and has the :html:`href` attribute pointing to the corresponding noteref hash.

	#.	In endnotes where the last block-level element is a :html:`<p>` element, the backlink goes at the end of the :html:`<p>` element, preceded by exactly one space.

	#.	In endnotes where the last block-level element is verse, quotation, or otherwise not plain prose text, the backlink goes in its own :html:`<p>` element following the last block-level element in the endnote.

#.	Endnotes with ending citations have those citations are wrapped in a :html:`<cite>` element, including any em-dashes. A space follows the :html:`<cite>` element, before the backlink.

.. class:: no-numbering

Examples
========

.. code:: html

	<p>... a continent that was not rent asunder by volcanic forces as was that legendary one of Atlantis in the Eastern Ocean.<a href="endnotes.xhtml#note-1" id="noteref-1" epub:type="noteref">1</a> My work in Java, in Papua, ...</p>

.. code:: html

	<?xml version="1.0" encoding="utf-8"?>
	<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" epub:prefix="z3998: http://www.daisy.org/z3998/2012/vocab/structure/, se: https://standardebooks.org/vocab/1.0" xml:lang="en-GB">
		<head>
			<title>Endnotes</title>
			<link href="../css/core.css" rel="stylesheet" type="text/css"/>
			<link href="../css/local.css" rel="stylesheet" type="text/css"/>
		</head>
		<body epub:type="backmatter">
			<section id="endnotes" epub:type="endnotes">
				<h2 epub:type="title">Endnotes</h2>
				<ol>
					<li id="note-1" epub:type="endnote">
						<p>For more detailed observations on these points refer to <abbr class="name">G.</abbr> Volkens, “Uber die Karolinen Insel Yap.” <cite>—<abbr class="name eoc">W. T. G.</abbr></cite> <a href="chapter-2.xhtml#noteref-1" epub:type="backlink">↩</a></p>
					</li>
					<li id="note-2" epub:type="endnote">
						<blockquote epub:type="z3998:verse">
							<p>
								<span>“Who never ceases still to strive,</span>
								<br/>
								<span>’Tis him we can deliver.”</span>
							</p>
						</blockquote>
						<p>
							<a href="chapter-4.xhtml#noteref-2" epub:type="backlink">↩</a>
						</p>
					</li>
				</ol>
			</section>
		</body>
	</html>

Glossaries
**********

Glossaries may be included if there are a large number of domain-specific terms that are unlikely to be in a common dictionary, or which have unique meanings to the work.

Glossaries follow the `EPUB Dictionaries and Glossaries 1.0 spec <http://idpf.org/epub/dict/epub-dict.html#sec-2.5.3>`__.

The glossary search key map file
================================

When including a glossary, a search key map file is required according to the `EPUB Dictionaries and Glossaries 1.0 spec <http://idpf.org/epub/dict/epub-dict.html#sec-2.5.3>`__.

#.	The search key map file is named :path:`./src/epub/glossary-search-key-map.xml`.

#.	The search key map file contains :html:`<value>` elements describing all stemmed variations of the parent search term that occur in the ebook. Variations that don't occur in the ebook are excluded.

#.	If a :html:`<match>` element only has one :html:`<value>` element, the :html:`<value>` element is removed in favor of :html:`<match value="...">`.

The glossary file
=================

#.	Glossaries are in an XHTML file named :path:`./src/epub/text/glossary.xhtml`.

#.	The glossary file has the :value:`backmatter` semantic inflection.

#.	The glossary file contains a single :html:`<section id="glossary" epub:type="glossary">` element, which may contain a title, followed by a :html:`<dl>` element containing the glossary entries. While the EPUB glossaries spec suggests the :value:`glossary` :html:`epub:type` attribute be placed on the :html:`<dl>` element, in a Standard Ebook it is placed on the :html:`<dl>` element’s parent :html:`<section>` element.

#.	All glossaries include the following CSS:

	.. code:: css

		dd + dt{
			margin-top: 1em;
		}

Glossary entries
================

#.	The :html:`<dl>` element contains sets of :html:`<dt>` and :html:`<dd>` elements.

#.	The :html:`<dt>` element has :html:`epub:type="glossterm"`.

#.	The :html:`<dt>` element contains a single :html:`<dfn>` element, which in turn contains the term to be defined.

#.	The :html:`<dd>` element has :html:`epub:type="glossdef"`.

#.	A :html:`<dd>` element appears after one or more :html:`<dt>` elements, and contains the definition for the preceding :html:`<dt>` element(s). It must contain at least one block-level child, usually :html:`<p>`.

	.. code:: html

		<dt epub:type="glossterm">
			<dfn>Coccus</dfn>
		</dt>
		<dd epub:type="glossdef">
			<p>The genus of Insects including the Cochineal. In these the male is a minute, winged fly, and the female generally a motionless, berrylike mass.</p>
		</dd>

#.	:html:`<dt>` may appear more than once for a single glossary entry, if different variations of a term have the same definition.

	.. code:: html

		<dt epub:type="glossterm">
			<dfn>Compositae</dfn>
		</dt>
		<dt epub:type="glossterm">
			<dfn>Compositous Plants</dfn>
		</dt>
		<dd epub:type="glossdef">
			<p>Plants in which the inflorescence consists of numerous small flowers (florets) brought together into a dense head, the base of which is enclosed by a common envelope. (Examples, the Daisy, Dandelion, <abbr class="eoc">etc.</abbr>)</p>
		</dd>
