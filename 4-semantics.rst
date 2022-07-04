#########
Semantics
#########

Semantics convey what an element or section *mean* or *are*, instead of merely conveying *how they are visually presented*.

For example, the following snippet visually presents a paragraph, followed by a quotation from a poem:

.. code:: html

	<div>“All done in the tying of a cravat,” Sir Percy had declared to his clique of admirers.</div>
	<div style="margin: 1em;">
		<div>“We seek him here, we seek him there,<br/>
		Those Frenchies seek him everywhere.<br/>
		Is he in heaven?⁠—Is he in hell,<br/>
		That demmed, elusive Pimpernel?”</div>
	</div>

While that snippet might *visually* present the text as a paragraph followed by a quotation of verse, the actual HTML tells us nothing about *what these lines of text actually are*.

Compare the above snippet to this next snippet, which renders almost identically but uses semantically-correct elements and epub’s semantic inflection to tell us *what the text is*:

.. code:: html

	<p>“All done in the tying of a cravat,” Sir Percy had declared to his clique of admirers.</p>
	<blockquote epub:type="z3998:poem">
		<p>
			<span>“We seek him here, we seek him there,</span>
			<br/>
			<span>Those Frenchies seek him everywhere.</span>
			<br/>
			<span>Is he in heaven?⁠—Is he in hell,</span>
			<br/>
			<span>That demmed, elusive Pimpernel?”</span>
		</p>
	</blockquote>

By inspecting the elements above, we can see that the first line is a semantic paragraph (:html:`<p>` stands for **p**\ aragraph, of course); the paragraph is followed by a semantic block quotation, which browsers automatically render with a margin; the quotation is a poem; the poem has one stanza; and there are four lines in the poem. (By SE convention, :html:`<p>` elements in verse are stanzas and :html:`<span>` elements are lines.)

Semantic Elements
*****************

Epub allows for the use of the full range of elements in the HTML5 spec. Each element has a semantic meaning, and each element in a Standard Ebook is carefully considered before use.

Below is an incomplete list of HTML5 elements and their semantic meanings. These are some of the most common elements encountered in an ebook.

Block-level elements
====================

Block-level elements are by default rendered with :css:`display: block;`. See the `complete list of block-level elements <https://developer.mozilla.org/en-US/docs/Web/HTML/Block-level_elements>`__.

#.	Sectioning block-level elements denote major structural divisions in a work.

	#.	:html:`<body>`: The top-level element in any XHTML file. Must contain a direct child that is either a :html:`<section>` or :html:`<article>`.

	#.	:html:`<section>`: A major structural division in a work. Typically a part, volume, chapter, or subchapter. Semantically a :html:`<section>` cannot stand alone, but is part of a larger work.

	#.	:html:`<article>`: An item in a larger work that could be pulled out of the work and serialized or syndicated separately. For example, a single poem in a poetry collection, or a single short story in a short story collection; but *not* a single poem in a larger novel.

#.	Other block-level elements have well-defined semantic meanings.

	#.	:html:`<p>`: A paragraph of text.

	#.	:html:`<blockquote>`: A quotation displayed on the block level. This may include non-speech “quotations” like business cards, headstones, telegrams, letters, and so on.

	#.	:html:`<figure>`: Encloses a photograph, chart, or illustration, represented with an :html:`<img>` element. Optionally includes a :html:`<figcaption>` element for a context-appropriate caption.

	#.	:html:`<figcaption>`: Only appears as a child of :html:`<figure>`. Represents a context-appropriate caption for the sibling :html:`<img>`. A caption *is not the same* as an :html:`<img>` element’s :html:`alt` text. :html:`alt` text is strictly a textual description of the image used for screen readers, whereas :html:`<figcaption>` has more freedom in its contents, depending on its context.

	#.	:html:`<header>`: Denotes a header section applying to its direct parent. :html:`<header>` is typically found in sections where there is additional header content besides the section title, but can also be used in :html:`<blockquote>`\ s or other block-level elements that require header styling.

	#.	:html:`<footer>`: Denotes a footer section applying to its direct parent. Typically used to denote signatures in sections like prefaces, forewords, letters, telegrams, and so on.

	#.	:html:`<hr/>`: Denotes a thematic break. :html:`<hr/>` *is not used* any place a black border is desired; it *strictly denotes* a thematic break.

	#.	:html:`<ol>`: Denotes an ordered list. Ordered lists are automatically numbered by the renderer.

	#.	:html:`<ul>`: Denotes an unordered list. Unordered lists are bulleted by the renderer.

	#.	:html:`<li>`: Denotes a list item in a parent :html:`<ol>` or :html:`<ul>`.

	#.	:html:`<table>`: Denotes a tabular section, for example when displaying tabular data, or reports or charts where a tabular appearance is desired.

#.	:html:`<div>` elements are almost never appropriate, as they have no semantic meaning. However, they may in rare occasions be used to group related elements in a situation where no other semantic element is appropriate.

Inline elements
===============

Inline elements are by default rendered with :css:`display: inline;`. See the `complete list of inline elements <https://developer.mozilla.org/en-US/docs/Web/HTML/Inline_elements>`__.

#.	:html:`<em>`: Text rendered in italics, with the semantic meaning of emphasized speech, or speech spoken in a different tone of voice; for example, a person shouting, or putting stress on a particular word.

#.	:html:`<i>`: Text rendered in italics, without any explicit semantic meaning. Because :html:`<i>` lacks semantic meaning, the :html:`epub:type` attribute is added with appropriate semantic inflection to describe the contents of the element.

	.. class:: corrected

		.. code:: html

			<p>The <abbr epub:type="z3998:initialism">H.M.S.</abbr> <i epub:type="se:name.vessel.ship">Bounty</i>.</p>

#.	:html:`<b>`: Text rendered in small caps, without any explicit semantic meaning. Because :html:`<b>` lacks semantic meaning, the :html:`epub:type` attribute can be added with appropriate semantic inflection to describe the contents of the element; however, unlike :html:`<i>`, it’s rare for :html:`<b>` to require semantic meaning, as it is generally used only for visual styling.

#.	:html:`<span>`: Plain inline text that requires specific styling or semantic meaning that cannot be achieved with any other semantically meaningful inline element. Typically used in conjunction with a :html:`class` or :html:`epub:type` attribute.

Semantic Inflection
*******************

The epub spec allows for `semantic inflection <https://www.w3.org/TR/epub-ssv-11/>`__, which is a way of adding semantic metadata to elements in the ebook document.

For example, an ebook producer may want to convey that the contents of a certain :html:`<section>` are part of a chapter. They would do that by using the :html:`epub:type` attribute:

.. code:: html

	<section epub:type="chapter">...</section>

#.	The epub spec includes a `vocabulary <https://www.w3.org/TR/epub-ssv-11/>`__ that can be used in the :html:`epub:type` attribute. This vocabulary has priority when selecting a semantic keyword, even if other vocabularies contain the same one.

#.	The epub spec might not contain a keyword necessary to describe the semantics of a particular element. In that case, the `z3998 vocabulary <http://www.daisy.org/z3998/2012/vocab/structure/>`__ is consulted next.

	Keywords using this vocabulary are preceded by the :value:`z3998` namespace.

	.. code:: html

		<blockquote epub:type="z3998:letter">...</blockquote>

#.	If the z3998 vocabulary doesn’t have an appropriate keyword, the `Standard Ebooks vocabulary </vocab/1.0>`__ is consulted next.

	Keywords using this vocabulary are preceded by the :value:`se` namespace.

	Unlike other vocabularies, the Standard Ebooks vocabulary is organized hierarchically. A complete vocabulary entry begins with the root vocabulary entry, with subsequent children separated by :value:`.`.

	.. code:: html

		The <abbr epub:type="z3998:initialism">H.M.S.</abbr> <i epub:type="se:name.vessel.ship">Bounty</i>.

#.	The :html:`epub:type` attribute can have multiple keywords separated by spaces, even if the vocabularies are different.

	.. code:: html

		<section epub:type="chapter z3998:letter">...</section>

#.	Child elements inherit the semantics of their parent element.

	In this example, both chapters are considered to be “non-fiction,” because they inherit it from the :html:`<body>` element:

	.. code:: html

		<body epub:type="z3998:non-fiction">
			<section id="chapter-1" epub:type="chapter">
				<h2 epub:type="ordinal z3998:roman">I</h2>
				...
			</section>
			<section id="chapter-2" epub:type="chapter">
				<h2 epub:type="ordinal z3998:roman">II</h2>
				...
			</section>
		</body>
