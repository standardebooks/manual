######################
General XHTML Patterns
######################

This section covers general patterns used when producing XHTML that are not specific to ebooks.

:html:`id` attributes
*********************

:html:`id` attributes of :html:`<section>` and :html:`<article>` elements
=========================================================================

#.	Each :html:`<section>` and :html:`<article>` element has an :html:`id` attribute.

#.	:html:`<section>` or :html:`<article>` elements that are direct children of the :html:`<body>` element have an :html:`id` attribute identical to the filename containing that :html:`<section>` or :html:`<article>`, without the trailing extension.

#.	In files containing multiple :html:`<section>` or :html:`<article>` elements, each of those elements has an :html:`id` attribute identical to what the filename *would* be if the section was in an individual file, without the trailing extension.

	.. class:: corrected

		.. code:: html

			<body epub:type="bodymatter z3998:fiction">
				<article id="the-fox-and-the-grapes" epub:type="se:short-story">
					<h2 epub:type="title">The Fox and the Grapes</h2>
					<p>...</p>
				</article>
				<article id="the-goose-that-laid-the-golden-eggs" epub:type="se:short-story">
					<h2 epub:type="title">The Goose That Laid the Golden Eggs</h2>
					<p>...</p>
				</article>
			</body>

:html:`id` attributes of other elements
=======================================

#.	:html:`id` attributes are generally used to identify parts of the document that a reader may wish to navigate to using a hash in the URL. That generally means major structural divisions. Therefore, elements that are not :html:`<section>` or :html:`<article>` elements do not have an :html:`id` attribute, unless a part of the ebook, like an endnote, refers to a specific point in the book, and a direct link is desirable.

#.	:html:`id` attributes are not used as hooks for CSS styling.

#.	If an element that is not a :html:`<section>` or :html:`<article>` requires an :html:`id` attribute, the attribute’s value is the name of the element followed by :value:`-N`, where :value:`N` is the sequence number of the element start at :value:`1`.

	.. class:: corrected

		.. code:: html

			<p>See <a href="#p-4">this paragraph</a> for more details.</p>
			<p>...</p>
			<p>...</p>
			<p id="p-4">...</p>
			<p>...</p>

#.	:html:`id` attributes on non-sectioning elements are unique across the entire ebook.

	#.	If an element requires an :html:`id` attribute that would conflict with one in a different file, the :html:`id` attribute an of the closest parent sectioning element, followed by :string:`-`, is prepended to each :html:`id` attribute to differentiate them.

		.. class:: wrong

			.. code:: html

				<!-- chapter-1.xhtml -->
				<section id="book-1" epub:type="division">
					<section id="chapter-1" epub:type="chapter">
						<p id="p-1">...</p>
					</section>
				</section>


				<!-- chapter-2.xhtml -->
				<section id="book-1" epub:type="division">
					<section id="chapter-2" epub:type="chapter">
						<p id="p-1">...</p>
					</section>
				</section>

		.. class:: corrected

			.. code:: html

				<!-- chapter-1.xhtml -->
				<section id="book-1" epub:type="division">
					<section id="chapter-1" epub:type="chapter">
						<p id="chapter-1-p-1">...</p>
					</section>
				</section>


				<!-- chapter-2.xhtml -->
				<section id="book-1" epub:type="division">
					<section id="chapter-2" epub:type="chapter">
						<p id="chapter-2-p-1">...</p>
					</section>
				</section>

:html:`class` attributes
************************

Classes denote a group of elements sharing a similar style.

#.	Classes are *not* used as single-use style hooks. There is almost always a way to compose a CSS selector to select a single element without the use of a one-off class.

	.. class:: wrong

		.. code:: css

			.business-card{
				border: 1px solid;
				padding: 1em;
			}

		.. code:: html

			<body epub:type="bodymatter z3998:fiction">
				<section epub:type="chapter">
					<p>...</p>
					<p>...</p>
					<p>...</p>
					<p>...</p>
					<blockquote class="business-card">
						<p>John Doe, <abbr class="eoc">Esq.</abbr></p>
					</blockquote>
				</section>
			</body>

	.. class:: corrected

		.. code:: css

			#chapter-3 blockquote{
				border: 1px solid;
				padding: 1em;
			}

		.. code:: html

			<body epub:type="bodymatter z3998:fiction">
				<section id="chapter-3" epub:type="chapter">
					<p>...</p>
					<p>...</p>
					<p>...</p>
					<p>...</p>
					<blockquote>
						<p>John Doe, <abbr class="eoc">Esq.</abbr></p>
					</blockquote>
				</section>
			</body>

#.	Classes are used to style a recurring *class* of elements, i.e. a class of element that appears more than once in an ebook.

	.. class:: corrected

		.. code:: css

			.business-card{
				border: 1px solid;
				padding: 1em;
			}

		.. code:: html

			<body epub:type="bodymatter z3998:fiction">
				<section id="chapter-3" epub:type="chapter">
					<p>...</p>
					<p>...</p>
					<blockquote class="business-card">
						<p>Jane Doe, <abbr class="eoc">Esq.</abbr></p>
					</blockquote>
					<p>...</p>
					<p>...</p>
					<blockquote class="business-card">
						<p>John Doe, <abbr class="eoc">Esq.</abbr></p>
					</blockquote>
				</section>
			</body>

#.	Class names describe *what* they are styling semantically, *not* the actual style the class is applying.

	.. class:: wrong

		.. code:: css

			.black-border{
				border: 1px solid;
				padding: 1em;
			}

	.. class:: corrected

		.. code:: css

			.business-card{
				border: 1px solid;
				padding: 1em;
			}

:html:`xml:lang` attributes
***************************

#.	When words are required to be pronounced in a language other than English, the :html:`xml:lang` attribute is used to indicate the IETF language tag in use.

	#.	The :html:`xml:lang` attribute is used even if a word is not required to be italicized. This allows screen readers to understand that a particular word or phrase should be pronounced in a certain way. A :html:`<span xml:lang="TAG">` element is used to wrap text that has non-English pronunciation but that does not need further visual styling.

	#.	The :html:`xml:lang` attribute is included in *any* word that requires special pronunciation, including names of places and titles of books.

	.. class:: corrected

		.. code:: html

			She opened the book titled <i epub:type="se:name.publication.book" xml:lang="la">Mortis Imago</i>.

	#.	The :html:`xml:lang` attribute is applied to the highest-level element possible. If italics are required and moving the :html:`xml:lang` attribute would also remove an :html:`<i>` element, the parent element can be styled with :css:`body [xml|lang]{ font-style: italic; }`.

	.. class:: wrong

		.. code:: html

			<blockquote>
				<p><i xml:lang="es">“Como estas?” el preguntó.</i></p>
				<p><i xml:lang="es">“Bien, gracias,” dijo ella.</i></p>
			</blockquote>

	.. class:: corrected

		.. code:: html

			<blockquote xml:lang="es">
				<p>“Como estas?” el preguntó.</p>
				<p>“Bien, gracias,” dijo ella.</p>
			</blockquote>

The :html:`<title>` element
***************************

#.	The :html:`<title>` element contains an appropriate description of the local file only. It does not contain the book title.

#.	The value of the title element is determined by the algorithm used to determine the file's ToC entry, except that no XHTML tags are allowed in the :html:`<title>` element.

Headers
*******

#.	:html:`<header>` elements have at least one direct child block-level element. This is usually a :html:`<p>` element, but not necessarily.

Ordered/numbered and unordered lists
************************************

#.	All :html:`<li>` children of :html:`<ol>` and :html:`<ul>` elements have at least one direct child block-level element. This is usually a :html:`<p>` element, but not necessarily; for example, a :html:`<blockquote>` element might also be appropriate.

	.. class:: wrong

		.. code:: html

			<ul>
				<li>Don’t forget to feed the pigs.</li>
			</ul>

	.. class:: corrected

		.. code:: html

			<ul>
				<li>
					<p>Don’t forget to feed the pigs.</p>
				</li>
			</ul>

Tables
******

#.	:html:`<table>` elements have a direct child :html:`<tbody>` element.

	.. class:: wrong

		.. code:: html

			<table>
				<tr>
					<td>1</td>
					<td>2</td>
				</tr>
			</table>

	.. class:: corrected

		.. code:: html

			<table>
				<tbody>
					<tr>
						<td>1</td>
						<td>2</td>
					</tr>
				</tbody>
			</table>

#.	:html:`<table>` elements may have an optional direct child :html:`<thead>` element, if a table heading is desired.

	#.	:html:`<th>` elements are used in :html:`<thead>` elements, instead of :html:`<td>`.

	#.	:html:`<th>` elements only appear in :html:`<thead>` elements, unless they contain the :html:`scope` attribute set to either :value:`row` or :value:`rowspan`. The :html:`scope` attribute set to those values may be used to semantically identify a table header which applies to a horizontal row instead of a vertical column.

#.	:html:`<table>` elements that are used to display tabular numerical data, for example columns of sums, have CSS styling for tabular numbers: :css:`{ font-variant-numeric: tabular-nums; }`.

	.. class:: corrected

		.. code:: css

			table td:last-child{
				text-align: right;
				font-variant-numeric: tabular-nums;
			}

		.. code:: html

			<table>
				<tbody>
					<tr>
						<td>Amount 1</td>
						<td>100</td>
					</tr>
					<tr>
						<td>Amount 2</td>
						<td>300</td>
					</tr>
					<tr>
						<td>Total</td>
						<td>400</td>
					</tr>
				</tbody>
			</table>

Blockquotes
***********

-	`See here for poetry </manual/VERSION/7-high-level-structural-patterns#7.5>`__.

#.	:html:`<blockquote>` elements must contain at least one block-level child, like :html:`<p>`.

#.	Blockquotes that have a citation include the citation as a direct child :html:`<cite>` element.

	.. code:: html

		<blockquote>
			<p>“All things are ready, if our mind be so.”</p>
			<cite>—<i epub:type="se:name.publication.play">Henry <span epub:type="z3998:roman">V</span></i></cite>
		</blockquote>

Definition lists
****************

Definition lists, i.e. combinations of the :html:`<dl>`, :html:`<dt>`, and :html:`<dd>` elements, are often found in glossaries.

`See here for glossaries </manual/VERSION/7-high-level-structural-patterns#7.11>`__.

#.	:html:`<dd>` elements have at least one direct child block-level element. This is usually a :html:`<p>` element, but not necessarily.
