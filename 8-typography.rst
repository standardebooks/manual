##########
Typography
##########

Section titles and ordinals
***************************

#.	Section ordinals in the body text are set in Roman numerals.

#.	Section titles are titlecased according to the output of :bash:`se titlecase`. Section titles are *not* all-caps or small-caps.

#.	Section titles do not have trailing periods.

#.	Chapter titles omit the word :string:`Chapter`, unless the word used is a stylistic choice for prose style purposes. Chapters with unique identifiers (i.e. not :string:`Chapter`, but something unique to the style of the book, like :string:`Book` or :string:`Stave`) *do* include that unique identifier in the title, wrapped in :html:`<span epub:type="label">`.

	.. class:: wrong

		.. code:: html

			<h2>Chapter <span epub:type="ordinal z3998:roman">II</span></h2>

	.. class:: corrected

		.. code:: html

			<h2 epub:type="ordinal z3998:roman">II</h2>

		.. code:: html

			<h2>
				<span epub:type="label">Stave</span>
				<span epub:type="ordinal z3998:roman">III</span>
			</h2>

	In special cases it may be desirable to retain :string:`Chapter` for clarity. For example, :italics:`Frankenstein </ebooks/mary-shelley/frankenstein>` has “Chapter” in titles to differentiate them from the “Letter” sections.

Italics
*******

#.	Using both italics *and* quotes (outside of the context of quoted dialog) is usually not necessary. Either one or the other is used, with rare exceptions.

#.	Words and phrases that require emphasis are italicized with the :html:`<em>` element.

	.. code:: html

		<p>“Perhaps <em>he</em> was there,” Raoul said, at last.</p>

#.	Strong emphasis, like shouting, may be set in small caps with the :html:`<strong>` element.

	.. code:: html

		<p>“<strong>Can’t</strong> I?” screamed the unhappy creature to himself.</p>

#.	When a short phrase within a longer clause is italicized, trailing punctuation that may belong to the containing clause is not italicized.

	.. class:: wrong

		.. code:: html

			<p>“Look at <em>that!</em>” she shouted.</p>

	.. class:: corrected

		.. code:: html

			<p>“Look at <em>that</em>!” she shouted.</p>

#.	When an entire clause is italicized, trailing punctuation *is* italicized, *unless* that trailing punctuation is a comma at the end of dialog.

	.. code:: html

		<p>“<em>Charge!</em>” she shouted.</p>

	.. code:: html

		<p>“<em>But I want to</em>,” she said.</p>

#.	Words written to be read as sounds are italicized with :html:`<i>`.

	.. code:: html

		<p>He could hear the dog barking: <i>Ruff, ruff, ruff!</i></p>

#.	A person's internal thoughts are italicized with unsemanticated :html:`<i>`.

	.. code:: html

		<p>The thought flashed to me: <i>it’s a city you’re firing at, not a plane</i>, and I flinched.</p>

Italicizing individual letters
==============================

#.	Individual letters that used in context as a `grapheme <https://www.merriam-webster.com/dictionary/grapheme>`__ are italicized with an :html:`<i epub:type="z3998:grapheme">` element. They are typically lowercased and not followed by periods.

	.. code:: html

		<p>He often rolled his <i epub:type="z3998:grapheme">r</i>’s.</p>

	#.	Plural graphemes are formed with :string:`’s`, to aid in clarity.

		.. class:: wrong

			.. code:: html

				<p>Her <i epub:type="z3998:grapheme">a</i>s were nasally.</p>

		.. class:: corrected

			.. code:: html

				<p>Her <i epub:type="z3998:grapheme">a</i>’s were nasally.</p>

#.	Individual letters that are *not* graphemes (for example letters that might be referring to names, the shapes of the letters themselves, musical notes or keys, or concepts) are *not* italicized.

	.. code:: html

		<p>...due to the loss of what is known in New England as the “L”: that long deep roofed adjunct usually built at right angles to the main house...</p>

	.. code:: html

		<p>She was learning her A.B.C.s.</p>

	.. code:: html

		<p>His trident had the shape of an E.</p>

	.. code:: html

		<p>The piece was in the key of C major.</p>

#.	The ordinal :string:`nth` is set with an italicized :string:`n`, without a hyphen.

	.. code:: html

		<p>The <i>n</i>th degree.</p>

Italicizing non-English words and phrases
=========================================

#.	Non-English words and phrases that are not in `Merriam-Webster <https://www.merriam-webster.com>`__ are italicized, unless they are in a non-Roman script like Chinese or Japanese.

	.. code:: html

		<p>The <i xml:lang="fr">corps de ballet</i> was flung into consternation.</p>

#.	Non-English words that are proper names, or are in proper names, are not italicized, unless the name itself would be italicized according to the rules for italicizing or quoting names and titles. If words in the name might be mispronounced in English pronunciation, they are wrapped in a :html:`<span xml:lang="LANGUAGE">` element to assist screen readers with pronunciation. Most proper names of people or places do not require this, but occasionally there may be some that do.

	.. class:: wrong

		.. code:: html

			<p>“<i xml:lang="fr">Où est le métro?</i>” he asked, and she pointed to <i xml:lang="fr">Place de Clichy</i>, next to the <i xml:lang="fr">Le Bon Petit Déjeuner</i> restaurant.</p>

	.. class:: corrected

		.. code:: html

			<p>“<i xml:lang="fr">Où est le métro?</i>” he asked, and she pointed to <span xml:lang="fr">Place de Clichy</span>, next to the <span xml:lang="fr">Le Bon Petit Déjeuner</span> restaurant.

#.	If certain non-English words are used so frequently in the text that italicizing them at each instance would be distracting to the reader, then only the first instance is italicized. Subsequent instances are wrapped in a :html:`<span xml:lang="LANGUAGE">` element.

#.	Words and phrases that are originally non-English in origin, but that can now be found in `Merriam-Webster <https://www.merriam-webster.com>`__, are not italicized.

	.. code:: html

		<p>Sir Percy’s bon mot had gone the round of the brilliant reception-rooms.</p>

#.	Inline-level italics are set using the :html:`<i>` element with an :html:`xml:lang` attribute corresponding to the correct `IETF language tag <https://en.wikipedia.org/wiki/IETF_language_tag>`__.

#.	Block-level italics are set using an :html:`xml:lang` attribute on the closest encompassing block element, with the style of :css:`font-style: italic`.

	In this example, note the additional namespace declaration, and that we target *descendants* of the :html:`<body>` element; otherwise, the entire :html:`<body>` element would receive italics!

	.. code:: css

		@namespace xml "http://www.w3.org/XML/1998/namespace";

		body [xml|lang]{
			font-style: italic;
		}

	.. code:: html

		<blockquote epub:type="z3998:verse" xml:lang="la">
			<p>
				<span>—gelidas leto scrutata medullas,</span>
				<br/>
				<span>Pulmonis rigidi stantes sine vulnere fibras</span>
				<br/>
				<span>Invenit, et vocem defuncto in corpore quaerit.</span>
			</p>
		</blockquote>


#.	Words that are in a non-English “alien” language (i.e. one that is made up, like in a science fiction or fantasy work) are italicized and given an IETF languate tag in a custom namespace. Custom namespaces begin consist of :value:`x-TAG`, where :value:`TAG` is a custom descriptor of 8 characters or less.

	.. code:: html

		<p>“<i xml:lang="x-arcturan">Dolm</i>,” said Haunte.</p>

Italicizing or quoting newly-used English words
===============================================

#.	When introducing new terms, non-English or technical terms are italicized, but terms composed of common English are set in quotation marks.

	.. code:: html

		<p>English whalers have given this the name “ice blink.”</p>
		<p>The soil consisted of that igneous gravel called <i>tuff</i>.</p>

#.	English neologisms in works where a special vocabulary is a regular part of the narrative are not italicized. For example science fiction works may necessarily contain made-up English technology words, and those are not italicized.

Italics in names and titles
===========================

#.	Place names, like pubs, bars, or buildings, are not quoted.

#.	The names of publications, music, and art that can stand alone are italicized; additionally, the names of transport vessels are italicized. These include, but are not limited to:

	-	Periodicals like magazines, newspapers, and journals.

	-	Publications like books, novels, plays, and pamphlets, *except* “holy texts,” like the Bible or books within the Bible.

	-	Long poems and ballads, like the :italics:`Iliad </ebooks/homer/the-iliad/william-cullen-bryant>`, that are book-length.

	-	Long musical compositions or audio, like operas, music albums, or radio shows.

	-	Long visual art, like films or a TV show series.

	-	Visual art, like paintings or sculptures.

	-	Transport vessels, like ships.

#.	The names of short publications, music, or art, that cannot stand alone and are typically part of a larger collection or work, are quoted. These include, but are not limited to:

	-	Short musical compositions or audio, like pop songs, arias, or an episode in a radio series.

	-	Short prose like novellas, shot stories, or short (i.e. not epic) poems.

	-	Chapter titles in a prose work.

	-	Essays or individual articles in a newspaper or journal.

	-	Short visual art, like short films or episodes in a TV series.

.. class:: no-numbering

Examples
--------

.. class:: wrong

	.. code:: html

		<p>He read “Candide” while having a pint at the “King’s Head.”</p>

.. class:: corrected

	.. code:: html

		<p>He read <i epub:type="se:name.publication.book">Candide</i> while having a pint at the King’s Head.</p>

Taxonomy
========

#.	Binomial names (generic, specific, and subspecific) are italicized with a :html:`<i>` element having the :value:`z3998:taxonomy` semantic inflection.

	.. code:: html

		<p>A bonobo monkey is <i epub:type="z3998:taxonomy">Pan paniscus</i>.</p>

#.	Family, order, class, phylum or division, and kingdom names are capitalized but not italicized.

	.. code:: html

		<p>A bonobo monkey is in the phylum Chordata, class Mammalia, order Primates.</p>

#.	If a taxonomic name is the same as the common name, it is not italicized.

#.	The second part of the binomial name follows the capitalization style of the source text. Modern usage requires lowercase, but older texts may set it in uppercase.

Exceptions
==========

#.	Epigraphs, bridgeheads, and some other types of heading matter are set in italics by default. Text that in a Roman-set context would be italicized (like non-English words or phrases, or titles of books) are thus set in Roman in that heading matter, to contrast against the default italics. However, if due to this rule the *entire block* would be set in Roman instead of italics, thus lending the block an unexpected appearance, then the contrasting Roman is discarded and the default italics are preserved.

	.. tip::

		This can usually be achieved by removing :html:`<i>` elements (which have no semantic meaning and merely indicate the desire for italics) and moving their :html:`epub:type` or :html:`xml:lang` attributes to their parent element.

	.. class:: wrong

		.. code:: css

			[epub|type~="epigraph"]{
				font-style: italic;
				/* ... */
			}

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

		.. code:: html

			<blockquote epub:type="epigraph">
				<p>“<i xml:lang="fr">En administration, toutes les sottises sont mères.</i>”</p>
				<cite><i epub:type="se:name.publication.book">Maximes</i>, <i xml:lang="la">fr</i> <abbr class="name">M. G.</abbr> De Levis.</cite>
			</blockquote>

	.. class:: corrected

		.. code:: css

			[epub|type~="epigraph"]{
				font-style: italic;
				/* ... */
			}

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

		.. code:: html

			<blockquote epub:type="epigraph">
				<p xml:lang="fr">“En administration, toutes les sottises sont mères.”</p>
				<cite><i epub:type="se:name.publication.book">Maximes</i>, <i xml:lang="la">fr</i> <abbr class="name">M. G.</abbr> De Levis.</cite>
			</blockquote>

Capitalization
**************

#.	In general, capitalization follows modern English style. Some very old works frequently capitalize nouns that today are no longer capitalized. These archaic capitalizations are removed, unless doing so would change the meaning of the work.

#.	Titlecasing, or the capitalization of titles, follows the formula used in the :bash:`se titlecase` tool.

#.	Text in all caps is almost never correct typography. Instead, such text is changed to the correct case and surround with a semantically-meaningful element like :html:`<em>` (for emphasis), :html:`<strong>` (for strong emphasis, like shouting) or :html:`<b>` (for unsemantic formatting required by the text). :html:`<strong>` and :html:`<b>` are styled in small-caps by default in Standard Ebooks.

	.. class:: wrong

		.. code:: html

			<p>The sign read BOB’S RESTAURANT.</p>

		.. code:: html

			<p>“CHARGE!” he cried.</p>

	.. class:: corrected

		.. code:: html

			<p>The sign read <b>Bob’s Restaurant</b>.</p>

		.. code:: html

			<p>“<strong>Charge!</strong>” he cried.</p>

#.	When something is addressed as an `apostrophe <https://www.merriam-webster.com/dictionary/apostrophe#dictionary-entry-2>`__, :string:`O` is capitalized.

	.. code:: html

		<p>I carried the bodies into the sea, O walker in the sea!</p>

#.	Names followed by a generational suffix, like :string:`Junior` or :string:`Senior`, have the suffix uppercased if the suffix is part of the person's name.

	Occasionally, :string:`junior` or :string:`senior` may be used to refer to a younger or elder person having the same last name, but not necessarily the same first name. In these cases, the suffix is lowercased as it is not part of their name, but rather describing their generational relation.

	.. code:: html

		<p>He talked to Bob Smith Junior.</p>
		<p>He talked to John Doe <abbr class="eoc">Jr.</abbr></p>
		<p>Madame Bovary junior was afraid of accidents for her husband.</p>

Indentation
***********

#.	Paragraphs that directly follow another paragraph are indented by 1em.

#.	The first line of body text in a section, or any text following a visible break in text flow (like a header, a scene break, a figurem etc.), is not indented, with the exception of block quotations.

	#.	Body text following a block quotation is indented only if the text begins a new semantic paragraph. Otherwise, if the body text following a block quotation is semantically part of the paragraph preceding the block quotation, it is not indented. Such non-indented paragraphs have :html:`class="continued"`, which removes the default indentation.

		.. code:: html

			<p>He sat down before a writing-table and, taking pen and ink, wrote on a slip of paper as follows:⁠—</p>
			<blockquote epub:type="z3998:letter">
				<p>The Bishop of Barchester is dead.</p>
			</blockquote>
			<p>“There,” said he. “Just take that to the telegraph office at the railway station and give it in as it is.”</p>

		.. code:: html

			<p>He opened the cover in which the message was enclosed and, having read it, he took his pen and wrote on the back of it⁠—</p>
			<blockquote epub:type="z3998:letter">
				<p epub:type="z3998:salutation">For the Earl of ⸻,</p>
				<footer>
					<p epub:type="z3998:valediction">With the Earl of ⸻’s compliments</p>
				</footer>
			</blockquote>
			<p class="continued">and sent it off again on its journey.</p>

Headers
*******

#.	Titles or subtitles that are *entirely* non-English-language are not italicized. However, they do have an :html:`xml:lang` attribute to assist screen readers in pronunciation. Titles or subtitles that are in English but contain non-English *components* have those components italicized according to the general rules for italics.

	.. code:: html

		<h2 epub:type="title" xml:lang="la">Ex Oblivione</h2>

		<h3 epub:type="title">
			<span epub:type="z3998:roman">XI</span>
			<span epub:type="subtitle">The <i epub:type="se:name.vessel.ship">Nautilus</i></span>
		</h3>

		<h2 epub:type="title">
			<span epub:type="z3998:roman">XXXV</span>
			<span epub:type="subtitle">Miss Thorne’s <i xml:lang="fr">Fête Champêtre</i></span>
		</h2>

		<h4 epub:type="title">
			<span epub:type="z3998:roman">XI</span>
			<span epub:type="subtitle" xml:lang="la">Christus Nos Liberavit</span>
		</h4>

Chapter headers
===============

#.	Epigraphs in chapters have the quote source set in small caps, without a leading em-dash and without a trailing period.

	.. class:: wrong

		.. code:: html

			<header>
				<h2 epub:type="title z3998:roman">II</h2>
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
				<h2 epub:type="title z3998:roman">II</h2>
				<blockquote epub:type="epigraph">
					<p>“Desire no more than to thy lot may fall. …”</p>
					<cite>Chaucer</cite>
				</blockquote>
			</header>

Ligatures
*********

Ligatures are two or more letters that are combined into a single letter, usually for stylistic purposes. In general they are not used in modern English spelling, and are replaced with their expanded characters.

Words in non-English languages like French may use ligatures to differentiate words or pronunciations. In these cases, ligatures are retained.

.. class:: wrong

	.. code:: html

		<p>Œdipus Rex</p>
		<p>Archæology</p>

.. class:: corrected

	.. code:: html

		<p>Oedipus Rex</p>
		<p>Archaeology</p>

Punctuation and spacing
***********************

#.	Sentences are single-spaced.

#.	Periods and commas are placed within quotation marks; i.e. American-style punctuation is used, not logical (AKA “British” or “new”) style.

	.. class:: wrong

		.. code:: html

			<p>Bosinney ventured: “It’s the first spring day”.</p>

	.. class:: corrected

		.. code:: html

			<p>Bosinney ventured: “It’s the first spring day.”</p>

#.	Ampersands are preceded by a no-break space (U+00A0).

	.. code:: html

		<p>The firm of Hawkins:ws:`nbsp`&amp; Harker.</p>

#.	Some older works include spaces in common contractions; these spaces are removed.

	.. See https://english.stackexchange.com/questions/217821/space-before-apostrophe

	.. class:: wrong

		.. code:: html

			<p>Would n’t it be nice to go out? It ’s such a nice day.</p>

	.. class:: corrected

		.. code:: html

			<p>Wouldn’t it be nice to go out? It’s such a nice day.</p>

Quotation marks
===============

#.	“Curly” or typographer’s quotes, both single and double, are always used instead of straight quotes. This is known as “American-style” quotation, which is different from British-style quotation which is also commonly found in both older and modern books.

	.. code:: html

		<p>“Don’t do it!” she shouted.</p>

#.	Quotation marks that are directly side-by-side are separated by a hair space (:utf:` ` or U+200A) character.

	.. code:: html

		<p>“:ws:`hairsp`‘Green?’ Is that what you said?” asked Dave.</p>

#.	Words with missing letters represent the missing letters with a right single quotation mark (:utf:`’` or U+2019) character to indicate elision.

	.. code:: html

		<p>He had pork ’n’ beans for dinner</p>

	#.	Elision is not to be confused with a glottal stop, which may sometimes occur in non-English languages like Hawaiian. Glottal stops that are not elided letters are represented with a turned comma (:utf:`ʻ` or U+02BB), *not* the similar-looking left single quotation mark (:utf:`‘` or U+2018).

		.. code:: html

			<p><i xml:lang="haw">ʻŌlelo Hawaiʻi</i></p>

	#.	Some last names in English were once contractions, and now are no longer contractions but actual last names in their own right. In these cases a left single quotation mark (:utf:`‘` or U+2018) is used to clarify pronunciation, but to make clear that the word is not a contraction.

		.. code:: html

			<p>His friends were James M‘Donald and Sam M‘Daniel.</p>

Ellipses
========

#.	The ellipses glyph (:utf:`…` or U+2026) is used for ellipses, instead of consecutive or spaced periods.

#.	When ellipses are used as suspension points (for example, to indicate dialog that pauses or trails off), the ellipses are not preceded by a comma.

	Ellipses used to indicate missing words in a quotation require keeping surrounding punctuation, including commas, as that punctuation is in the original quotation.

#.	A word joiner (U+2060), followed by a hair space (:utf:` ` or U+200A) glyph, followed by another word joiner (U+2060), are located *before* all ellipses that do not begin a paragraph, and that are not directly preceded by :utf:`“`.

#.	A regular space is located *after* all ellipses do not end a paragraph and that are not followed by punctuation.

#.	A hair space (:utf:` ` or U+200A) glyph is located between an ellipses and any punctuation that follows directly after the ellipses, *unless* that punctuation is a quotation mark, in which case there is no space at all between the ellipses and the quotation mark.

	.. code:: html

		<p>“I’m so hungry:ws:`wj`:ws:`hairsp`:ws:`wj`…:ws:`hairsp`! What were you saying about eating:ws:`wj`:ws:`hairsp`:ws:`wj`…?”

Dashes
======

There are many kinds of dashes, and the run-of-the-mill hyphen is often not the correct dash to use. In particular, hyphens are not used for things like date ranges, phone numbers, or negative numbers.

#.	Dashes of all types do not have white space around them.

#.	Figure dashes (:utf:`‒` or U+2012) are used to indicate a dash in numbers that aren’t a range, like phone numbers.

	.. code:: html

		<p>His number is 555‒1234.</p>

#.	Hyphens (:utf:`-` or U+002D) are used to join words, including double-barrel names, or to separate syllables in a word.

	.. code:: html

		<p>Pre-	and post-natal.</p>

	.. code:: html

		<p>The Smoot-Hawley act.</p>

#.	Minus sign glyphs (:utf:`−` or U+2212) are used to indicate negative numbers, and are used in mathematical equations instead of hyphens to represent the “subtraction” operator.

	.. code:: html

		<p>It was −5° out yesterday!</p>

	.. code:: html

		<p>5 − 2 = 3</p>

#.	En-dashes (:utf:`–` or U+2013) are used to indicate a numerical or date range; to indicate a relationships where two concepts are connected by the word “to,” for example a distance between locations or a range between numbers; or to indicate a connection in location between two places.

	.. code:: html

		<p>We talked 2–3 days ago.</p>

	.. code:: html

		<p>We took the Berlin–Munich train yesterday.</p>

	.. code:: html

		<p>I saw the torpedo-boat in the Ems⁠–⁠Jade Canal.</p>

#.	Non-break hyphens (:utf:`‑` or U+2011) are used when a single word is stretched out by a speaker for prosaic effect.

	.. code:: html

		<p>When you wa‑ake, you shall ha‑ave, all the pretty little hawsiz—</p>

	.. warning::

		When adding non-breaking hyphens for obscured letters, beware that :bash:`se typogrify` will incorrectly convert them to regular hyphens!

Em-dashes
---------

Em-dashes (:utf:`—` or U+2014) are typically used to offset parenthetical phrases.

#.	Em-dashes are preceded by the invisible word joiner glyph (U+2060).

#.	Interruption in dialog is set by a single em-dash, not two em-dashes or a two-em-dash.

	.. class:: wrong

		.. code:: html

			<p>“I wouldn’t go as far as that, not myself, but:ws:`wj`——”</p>

	.. class:: corrected

		.. code:: html

			<p>“I wouldn’t go as far as that, not myself, but:ws:`wj`—”</p>

Partially-obscured words
------------------------

#.	Em-dashes are used for partially-obscured years.

	.. code:: html

		<p>It was the year 19:ws:`wj`— in the town of Metropolis.</p>

#.	A regular hyphen is used in partially obscured years where only the last number is obscured.

	.. code:: html

		<p>It was the year 192-	in the town of Metropolis.</p>

#.	A non-breaking hyphen (:utf:`‑` or U+2011) is used when a single letter is obscured in a word.

	.. code:: html

		<p>He performed Mozart’s famous canon, “Leck mich im A‑sche.”</p>

	.. warning::

		When adding non-breaking hyphens for obscured letters, beware that :bash:`se typogrify` will incorrectly convert them to regular hyphens!

#.	A two-em-dash (:utf:`⸺` or U+2E3A) preceded by a word joiner glyph (U+2060) is used in *partially* obscured word.

	.. code:: html

		<p>Sally J:ws:`wj`⸺ walked through town.</p>

#.	A three-em-dash (:utf:`⸻` or U+2E3B) is used for *completely* obscured words.

	.. code:: html

		<p>It was night in the town of ⸻.</p>

Numbers, measurements, and math
*******************************

#.	Coordinates are set with the prime (:utf:`′` or U+2032) or double prime (:utf:`″` or U+2033) glyphs, *not* single or double quotes.

	.. class:: wrong

		.. code:: html

			<p><abbr>Lat.</abbr> 27° 0' <abbr class="compass">N.</abbr>, <abbr>long.</abbr> 20° 1' <abbr class="compass eoc">W.</abbr></p>
			<p><abbr>Lat.</abbr> 27° 0’ <abbr class="compass">N.</abbr>, <abbr>long.</abbr> 20° 1’ <abbr class="compass eoc">W.</abbr></p>

	.. class:: corrected

		.. code:: html

			<p><abbr>Lat.</abbr> 27° 0′ <abbr class="compass">N.</abbr>, <abbr>long.</abbr> 20° 1′ <abbr class="compass eoc">W.</abbr></p>

#.	Ordinals for Arabic numbers are as follows: :string:`st`, :string:`nd`, :string:`rd`, :string:`th`.

	.. class:: wrong

		.. code:: html

			<p>The 1st, 2d, 3d, 4th.</p>

	.. class:: corrected

		.. code:: html

			<p>The 1st, 2nd, 3rd, 4th.</p>

#.	Numbers in a non-mathematical context are spelled out if they are less than or equal to 100. Numbers over 100 are set with digits.

	.. code:: html

		<p>“They had a gun on the West Front⁠—a seventy-five,” said O’Keefe.</p>
		<p>Allowing her 12,000 miles of straight-line travel through Uranus’ frigid soupy atmosphere.</p>

	#.	If a series of numbers is close together in a sentence, and one would be spelled out but another wouldn’t, spell out all numbers within that context to maintain visual consistency.

		.. class:: wrong

			.. code:: html

				<p>There the Gulf Stream is 75 miles wide and two hundred ten meters deep.</p>

		.. class:: corrected

			.. code:: html

				<p>There the Gulf Stream is seventy-five miles wide and two hundred ten meters deep.</p>

	#.	The *plural* form of spelled-out numbers is formed without an apostrophe. However the *possessive* or *contracted* form does include an apostrophe.

		.. class:: wrong

			.. code:: html

				<p>There were, the other answered, half a dozen two four two’s.</p>

		.. class:: corrected

			.. code:: html

				<p>There were, the other answered, half a dozen two four twos.</p>

				<p>Twice two’s four, and a stone’s a stone.</p>

				<p>He was allowed a day or two’s shooting in September.</p>

Roman numerals
==============

#.	Roman numerals are not followed by trailing periods, except for grammatical reasons.

#.	Roman numerals are set using uppercase ASCII, not the Unicode Roman numeral glyphs.

#.	Roman numerals are not followed by ordinal indicators.

	.. class:: wrong

		.. code:: html

			<p>Henry <span epub:type="z3998:roman">VIII</span>th had six wives.</p>

	.. class:: corrected

		.. code:: html

			<p>Henry <span epub:type="z3998:roman">VIII</span> had six wives.</p>

Fractions
=========

#.	Fractions are set in their appropriate Unicode glyph, if a glyph available; for example, :utf:`½`, :utf:`¼`, :utf:`¾` and U+00BC–U+00BE and U+2150–U+2189.

	.. class:: wrong

		.. code:: html

			<p>I need 1/4 cup of sugar.</p>

	.. class:: corrected

		.. code:: html

			<p>I need ¼ cup of sugar.</p>

#.	If a fraction doesn’t have a corresponding Unicode glyph, it is composed using the fraction slash Unicode glyph (:utf:`⁄` or U+2044) and superscript/subscript Unicode numbers. See `this Wikipedia entry for more details <https://en.wikipedia.org/wiki/Unicode_subscripts_and_superscripts>`__.

	.. class:: wrong

		.. code:: html

			<p>Roughly 6/10 of a mile.</p>

	.. class:: corrected

		.. code:: html

			<p>Roughly ⁶⁄₁₀ of a mile.</p>

#.	There is no space between a whole number and its fraction.

	.. class:: corrected

		.. code:: html

			<p>There are 365¼ days in a year.</p>

Measurements
============

#.	Dimension measurements are set using the Unicode multiplication glyph (:utf:`×` or U+00D7), *not* the ASCII letter :utf:`x` or :utf:`X`.

	.. class:: wrong

		.. code:: html

			<p>The board was 4 x 3 x 7 feet.</p>

	.. class:: corrected

		.. code:: html

			<p>The board was 4 × 3 × 7 feet.</p>

#.	Feet and inches in shorthand are set using the prime (:utf:`′` or U+2032) or double prime (:utf:`″` or U+2033) glyphs (*not* single or double quotes), with a no-break space (U+00A0) separating consecutive feet and inch measurements.

	.. class:: wrong

		.. code:: html

			<p>He was 6':ws:`nbsp`1" in height.</p>
			<p>He was 6’:ws:`nbsp`1” in height.</p>

	.. class:: corrected

		.. code:: html

			<p>He was 6′:ws:`nbsp`1″ in height.</p>

#.	When forming a compound of a number and unit of measurement in which the measurement is abbreviated, the number and unit of measurement are separated with a no-break space (U+00A0), *not* a dash. For exceptions in money, see `8.8.8 <#8.8.8>`__.

	.. class:: wrong

		.. code:: html

			<p>A 12-<abbr>mm</abbr> pistol.</p>

	.. class:: corrected

		.. code:: html

			<p>A 12:ws:`nbsp`<abbr>mm</abbr> pistol.</p>

Punctuation in abbreviated measurements
---------------------------------------

`See here for general abbreviation rules that also apply to measurements </manual/VERSION/8-typography#8.10>`__.

#.	Abbreviated `SI units <https://en.wikipedia.org/wiki/International_System_of_Units>`__ are set in lowercase without periods. They are not initialisms.

	.. code:: html

		<p>A 12:ws:`nbsp`<abbr>mm</abbr> pistol.</p>

#.	Abbreviated `English <https://en.wikipedia.org/wiki/English_units>`__, `Imperial <https://en.wikipedia.org/wiki/Imperial_units>`__, or `US customary <https://en.wikipedia.org/wiki/United_States_customary_units>`__ units that are one word are set in lowercase with a trailing period. They are not initialisms.

	.. code:: html

		<p>We had two 9:ws:`nbsp`<abbr>ft.</abbr> sledges, of 41:ws:`nbsp`<abbr>lbs.</abbr> each.</p>

	The one exception is :string:`G` (i.e. :string:`G-force`), which is an initialism that is set without a period.

	.. code:: html

		<p>There’s a force of over a hundred thousand <abbr class="initialism">G</abbr>’s.</p>

#.	Abbreviated English, Imperial, or US customary units that are more than one word (like :string:`hp` for :string:`horse power` or :string:`mph` for :string:`miles per hour`) are set in lowercase without periods. They are not initialisms.

	.. code:: html

		<p>He drove his 40:ws:`nbsp`<abbr>hp</abbr> car at 20:ws:`nbsp`<abbr>mph</abbr>.</p>

Math
====

#.	In works that are not math-oriented or that don’t have a significant amount of mathematical equations, equations are set using regular HTML and Unicode.

	#.	Operators and operands in mathematical equations are separated by a space.

		.. class:: wrong

			.. code:: html

				<p>6−2+2=6</p>

		.. class:: corrected

			.. code:: html

				<p>6 − 2 + 2 = 6</p>

	#.	Operators like subtraction (:utf:`−` or U+2212), multiplication (:utf:`×` or U+00D7), and equivalence (:utf:`≡` or U+2261) are set using their corresponding Unicode glyphs, *not* a hyphen or :utf:`x`. Almost all mathematical operators have a corresponding special Unicode glyph.

		.. class:: wrong

			.. code:: html

				<p>6 -	2 x 2 == 2</p>

		.. class:: corrected

			.. code:: html

				<p>6 − 2 × 2 ≡ 2</p>

#.	In works that are math-oriented or that have a significant amount of math, *all* variables, equations, and other mathematical objects are set using MathML.

	#.	When MathML is used in a file, the :value:`m` namespace is declared at the top of the file and used for all subsequent MathML code, as follows:

		.. code:: html

			xmlns:m="http://www.w3.org/1998/Math/MathML"

		This namespace is declared and used even if there is just a single MathML equation in a file.

		.. class:: wrong

			.. code:: html

				<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" ub:prefix="z3998: http://www.daisy.org/z3998/2012/vocab/structure/, se: https://standardebooks.org/vocab/1.0" xml:lang="en-GB">
				...
				<p>
					<math xmlns="http://www.w3.org/1998/Math/MathML" alttext="x">
						<ci>x</ci>
					</math>
				</p>

		.. class:: corrected

			.. code:: html

				<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xmlns:m="http://www.w3.org/1998/Math/MathML" epub:prefix="z3998: http://www.daisy.org/z3998/2012/vocab/structure/, se: https://standardebooks.org/vocab/1.0" xml:lang="en-GB">
				...
				<p>
					<m:math alttext="x">
						<m:ci>x</m:ci>
					</m:math>
				</p>

	#.	When possible, Content MathML is used over Presentational MathML. (This may not always be possible depending on the complexity of the work.)

		.. class:: corrected

			.. code:: html

				<p>
					<m:math alttext="x + 1 = y">
						<m:apply>
							<m:equals/>
							<m:apply>
								<m:plus/>
								<m:ci>x</m:ci>
								<m:cn>1</m:cn>
							</m:apply>
							<m:ci>y</m:ci>
						</m:apply>
					</m:math>
				</p>

	#.	Each :html:`<m:math>` element has an :html:`alttext` attribute.

		#.	The :html:`alttext` attribute describes the contents in the element in plain-text Unicode according to the rules in `this specification <https://www.unicode.org/notes/tn28/UTN28-PlainTextMath.pdf>`__.

		#.	Operators in the :html:`alttext` attribute are surrounded by a single space.

			.. class:: wrong

				.. code:: html

					<p>
						<m:math alttext="x+1=y">
							<m:apply>
								<m:equals/>
								<m:apply>
									<m:plus/>
									<m:ci>x</m:ci>
									<m:cn>1</m:cn>
								</m:apply>
								<m:ci>y</m:ci>
							</m:apply>
						</m:math>
					</p>

			.. class:: corrected

				.. code:: html

					<p>
						<m:math alttext="x + 1 = y">
							<m:apply>
								<m:equals/>
								<m:apply>
									<m:plus/>
									<m:ci>x</m:ci>
									<m:cn>1</m:cn>
								</m:apply>
								<m:ci>y</m:ci>
							</m:apply>
						</m:math>
					</p>

	#.	When using Presentational MathML, :html:`<m:mrow>` is used to group subexpressions, but only when necessary. Many elements in MathML, like :html:`<m:math>` and :html:`<m:mtd>`, *imply* :html:`<m:mrow>`, and redundant elements are not desirable. See `this section of the MathML spec <https://www.w3.org/Math/draft-spec/mathml.html#chapter3_presm.reqarg>`__ for more details.

		.. class:: wrong

			.. code:: html

				<p>
					<m:math alttext="x">
						<m:mrow>
							<m:mi>x</m:mi>
						</m:mrow>
					</m:math>
				</p>

		.. class:: corrected

			.. code:: html

				<p>
					<m:math alttext="x">
						<m:mi>x</m:mi>
					</m:math>
				</p>

	#.	If a Presentational MathML expression contains a function, the invisible Unicode function application glyph (U+2061) is used as an operator between the function name and its operand. This element looks exactly like the following, including the comment for readability: :html:`<m:mo>⁡<!--hidden U+2061 function application--></m:mo>`. (Note that the preceding element contains an *invisible* Unicode character! It can be revealed with the :bash:`se unicode-names` tool.)

		.. class:: wrong

			.. code:: html

				<p>
					<m:math alttext="f(x)">
						<m:mi>f</m:mi>
						<m:row>
							<m:mo fence="true">(</m:mo>
							<m:mi>x</m:mi>
							<m:mo fence="true">)</m:mo>
						</m:row>
					</m:math>
				</p>

		.. class:: corrected

			.. code:: html

				<p>
					<m:math alttext="f(x)">
						<m:mi>f</m:mi>
						<m:mo>⁡:utf:`U+2061`<!--hidden U+2061 function application--></m:mo>
						<m:row>
							<m:mo fence="true">(</m:mo>
							<m:mi>x</m:mi>
							<m:mo fence="true">)</m:mo>
						</m:row>
					</m:math>
				</p>

	#.	Expressions grouped by parenthesis or brackets are wrapped in an :html:`<m:row>` element, and fence characters are set using the :html:`<m:mo fence="true">` element. Separators are set using the :html:`<m:mo separator="true">` element. :html:`<m:mfenced>`, which used to imply both fences and separators, is deprecated in the MathML spec and thus is not used.

		.. class:: wrong

			.. code:: html

				<p>
					<m:math alttext="f(x,y)">
						<m:mi>f</m:mi>
						<m:mo>⁡:utf:`U+2061`<!--hidden U+2061 function application--></m:mo>
						<m:fenced>
							<m:mi>x</m:mi>
							<m:mi>y</m:mi>
						</m:fenced>
					</m:math>
				</p>

		.. class:: corrected

			.. code:: html

				<p>
					<m:math alttext="f(x,y)">
						<m:mi>f</m:mi>
						<m:mo>⁡:utf:`U+2061`<!--hidden U+2061 function application--></m:mo>
						<m:row>
							<m:mo fence="true">(</m:mo>
							<m:mi>x</m:mi>
							<m:mo separator="true">,</m:mo>
							<m:mi>x</m:mi>
							<m:mo fence="true">)</m:mo>
						</m:row>
					</m:math>
				</p>

	#.	If a MathML variable includes an overline, it is set by combining the variable’s normal Unicode glyph and the Unicode overline glyph (:utf:`‾` or U+203E) in a :html:`<m:mover>` element. However in the :html:`alttext` attribute, the Unicode overline combining mark (U+0305) is used to represent the overline in Unicode.

		.. class:: corrected

			.. code:: html

				<p>
					<m:math alttext="x̅">
						<m:mover>
							<m:mi>x</m:mi>
							<m:mo>‾</m:mo>
						</m:mover>
					</m:math>
				</p>

Money
=====

#.	Typographically-correct symbols are used for currency symbols.

	.. class:: wrong

		.. code:: html

			<p>The exchange rate was L2 for $1.</p>

	.. class:: corrected

		.. code:: html

			<p>The exchange rate was £2 for $1.</p>

#.	Currency symbols are not abbreviations.

£sd shorthand
-------------

`£sd shorthand <https://en.wikipedia.org/wiki/%C2%A3sd>`__ is a way of denoting pre-decimal currencies (pounds, shillings, and pence) common in England and other parts of the world until the 1970s.

#.	There is no white space between a number and an £sd currency symbol.

	.. class:: wrong

		.. code:: html

			<p>£ 14 8 s. 2 d. is known as a “tuppence.”</p>

	.. class:: corrected

		.. code:: html

			<p>£14 8<abbr>s.</abbr> 2<abbr>d.</abbr> is known as a “tuppence.”</p>

#.	Letters used in £sd shorthand are wrapped in :html:`<abbr>` elements.

	.. class:: wrong

		.. code:: html

			<p>£14 8s. 2d. is known as a “tuppence.”</p>

	.. class:: corrected

		.. code:: html

			<p>£14 8<abbr>s.</abbr> 2<abbr>d.</abbr> is known as a “tuppence.”</p>

Latinisms
*********

-	`See here for times </manual/VERSION/8-typography#8.11>`__.

#.	Latinisms (except :string:`sic`) that can be found in a modern dictionary are not italicized. Examples include :string:`e.g.`, :string:`i.e.`, :string:`ad hoc`, :string:`viz.`, :string:`ibid.`, :string:`etc.`. The exception is :string:`sic`, which is always italicized.

#.	Whole passages of Latin language and Latinisms that aren’t found in a modern dictionary are italicized.

#.	:string:`&c.` is not used, and is replaced with :string:`etc.`.

#.	For :string:`Ibid.`, `see Endnotes </manual/VERSION/7-high-level-structural-patterns#7.9>`__.

#.	Latinisms that are abbreviations are set in lowercase with periods between words and no spaces between them, except :string:`BC`, :string:`AD`, :string:`BCE`, and :string:`CE`, which are set without periods, in small caps, and wrapped with :html:`<abbr class="era">`:

	.. code:: css

		abbr.era{
			font-variant: all-small-caps;
		}

	.. code:: html

		<p>Julius Caesar was born around 100 <abbr class="era">BC</abbr>.</p>

Initials and abbreviations
**************************

-	`See here for temperatures </manual/VERSION/8-typography#8.13>`__.

-	`See here for times </manual/VERSION/8-typography#8.11>`__.

-	`See here for Latinisms including BC and AD </manual/VERSION/8-typography#8.9>`__.

-	`See here for measurements </manual/VERSION/8-typography#8.8>`__.

#.	Acronyms (terms made up of initials and pronounced as one word, like :string:`NASA`, :string:`SCUBA`, or :string:`NATO`) are set in small caps, without periods, and are wrapped in an :html:`<abbr class="acronym">` element with corresponding CSS.

	.. code:: css

		abbr.acronym{
			font-variant: all-small-caps;
		}

	.. code:: html

		<p>He was hired by <abbr class="acronym">NASA</abbr> last week.</p>

#.	Initialisms (terms made up of initials in which each initial is pronounced separately, like :string:`M.P.`, :string:`P.S.`, or :string:`U.S.S.R.`) are set with periods and without spaces (with some exceptions that follow) and are wrapped in an :html:`<abbr class="initialism">` element.

	.. code:: html

		<p>He was hired by the <abbr class="initialism">U.S.</abbr> <abbr class="initialism">F.B.I.</abbr> last week.</p>

#.	When an abbreviation that is not an acronym contains a terminal period, its :html:`<abbr>` element has the additional :value:`eoc` class (End of Clause) if the terminal period is also the last period in clause. Such sentences do not have two consecutive periods.

	.. code:: html

		<p>She loved Italian food like pizza, pasta, <abbr class="eoc">etc.</abbr></p>

	.. code:: html

		<p>He lists his name alphabetically as Johnson, <abbr class="name eoc">R. A.</abbr></p>

	.. code:: html

		<p>His favorite hobby was <abbr class="acronym">SCUBA</abbr>.</p>

#.	Initials of people’s names are each separated by periods and spaces. The group of initials is wrapped in an :html:`<abbr class="name">` element.

	.. code:: html

		<p><abbr class="name">H. P.</abbr> Lovecraft described himself as an aged antiquarian.</p>

#.	Academic degrees are wrapped in an :html:`<abbr class="degree">` element. Degrees that consist of initials are set with a period between each initial. Degrees that consist of initials followed by abbreviated words are set with a hair space before the word.

	.. code:: html

		<p>Judith Douglas, <abbr class="degree eoc">D.D.S</abbr></p>
		<p>Abraham Van Helsing, <abbr class="degree">M.D.</abbr>, <abbr class="degree">D.:ws:`hairsp`Ph.</abbr>, <abbr class="degree">D.:ws:`hairsp`Lit.</abbr>, <abbr>etc.</abbr>, <abbr class="eoc">etc.</abbr></p>

	#.	Some degrees are exceptions:

		- :string:`LL.D.` does not have a period in :string:`LL`, because it indicates the plural :string:`Legum`.

#.	Postal codes and abbreviated US states are set in all caps, without periods or spaces, and are wrapped in an :html:`<abbr class="postal">` element.

	.. code:: html

		<p>Washington <abbr class="postal">DC</abbr>.</p>

#.	Abbreviations that are abbreviations of a single word, and that are not acronyms or initialisms (like :string:`Mr.`, :string:`Mrs.`, or :string:`lbs.`) are set with :html:`<abbr>`.

	#.	Abbreviations ending in a lowercase letter are set without spaces between the letters, and have a trailing period.

	#.	Abbreviations without lowercase letters are set without spaces and without a trailing period.

	#.	Abbreviations that describes the next word, like :string:`Mr.`, :string:`Mrs.`, :string:`Mt.`, and :string:`St.`, are set with a no-break space (U+00A0) between the abbreviation and its target.

		.. code:: html

			<p>He called on <abbr>Mrs.</abbr>:ws:`nbsp`Jones yesterday.</p>

#.	Compass points are separated by periods and spaces. The group of points are wrapped in an :html:`<abbr class="compass">` element.

	.. code:: html

		<p>He traveled <abbr class="compass">S.</abbr>, <abbr class="compass">N. W.</abbr>, then <abbr class="compass eoc">E. S. E.</abbr></p>

Exceptions that are not abbreviations
=====================================

#.	The following are not abbreviations, and are set without periods or spaces.

	-	:string:`OK`

	-	:string:`SOS`

#.	The following are initialisms, but are set without periods or spaces:

	-	:string:`TV`, i.e. :string:`television`.

	-	:string:`AC` and :string:`DC`, when referring to electrical current.

	-	:string:`G`, when used in the sense of :string:`G-force`. Also see `8.8.5.4.2 <#8.8.5.4.2>`__.

	-	Stock ticker symbols.

		.. code:: html

			<p>She bought 125 shares of <abbr class="initialism">XYZ</abbr> corporation.</p>

#.	The following are abbreviations, but are not initialisms. Unlike almost all other abbreviations, they are in all caps and only have a period at the end.

	-	:string:`MS.` (manuscript)

	-	:string:`MSS.` (manuscripts)

	-	:string:`M.` (Monsieur)

	-	:string:`MM.` (Messieurs)

	.. code:: html

		<p><abbr>MM.</abbr>:ws:`nbsp`Guy and Luc were putting the finishing touches on the <abbr>MS.</abbr> of their new novel.</p>

#.	:string:`A.B.C.`, when used in the sense of the alphabet, is not an abbreviation, and is set with periods between the letters. But other uses, like :string:`A.B.C. shops`, *are* abbreviations. (The abbreviation in :string:`A.B.C. shop` stands for “`Australian Broadcasting Corporation <https://en.wikipedia.org/wiki/ABC_Commercial>`__.”)

	.. code:: html

		<p>She was learning her A.B.C.s</p>
		<p>He stopped by the <abbr class="initialism">A.B.C.</abbr> shop.</p>

Other exceptions
================

#.	The abbreviations :string:`1D`, :string:`2D`, :string:`3D`, and :string:`4D`, meaning first, second, third, and fourth dimensions, are abbreviations but do not have a trailing period.

#.	The words :string:`recto` and :string:`verso` are sometimes abbreviated with an initial and a superscript :string:`o`. They are regular abbreviations, set without periods, and the :string:`o` is superscripted with :html:`<sup>`.

	.. code:: html

		<p><abbr>Ch.</abbr> 1, <abbr>fol.</abbr> 2 <abbr>r<sup>o</sup></abbr>.</p>

Times
*****

#.	Times in a.m. and p.m. format are set in lowercase, with periods, and without spaces.

#.	:string:`a.m.` and :string:`p.m.` are wrapped in an :html:`<abbr class="time">` element.

Times as digits
===============

#.	Digits in times are separated by a colon, not a period or comma.

#.	Times written in digits followed by :string:`a.m.` or :string:`p.m.` are set with a no-break space (U+00A0) between the digit and :string:`a.m.` or :string:`p.m.`.

	.. code:: html

		<p>He called at 6:40:ws:`nbsp`<abbr class="time eoc">a.m.</abbr></p>

Times as words
==============

#.	Words in a spelled-out time are separated by spaces, unless they appear before a noun, where they are separated by a hyphen.

	.. code:: html

		<p>He arrived at five thirty.</p>

	.. code:: html

		<p>They took the twelve-thirty train.</p>

#.	Times written in words followed by :string:`a.m.` or :string:`p.m.` are set with a regular space between the time and :string:`a.m.` or :string:`p.m.`.

	.. code:: html

		<p>She wasn’t up till seven <abbr class="time eoc">a.m.</abbr></p>

#.	Military times that are spelled out (for example, in dialog) are set with dashes. Leading zeros are spelled out as :string:`oh`.

	.. code:: html

		<p>He arrived at oh-nine-hundred.</p>

Chemicals and compounds
***********************

#.	Molecular compounds are set in Roman, without spaces, and wrapped in an :html:`<abbr class="compound">` element.

	.. code:: html

		<p>He put extra <abbr class="compound">NaCl</abbr> on his dinner.</p>

#.	Elements in a molecular compound are capitalized according to their listing in the periodic table.

#.	Amounts of an element in a molecular compound are set in subscript with a :html:`<sub>` element.

	.. code:: html

		<p>She drank eight glasses of <abbr class="compound">H<sub>2</sub>O</abbr> a day.</p>

Temperatures
************

#.	The minus sign glyph (:utf:`−` or U+2212), not the hyphen glyph, is used to indicate negative numbers.

#.	Either the degree glyph (:utf:`°` or U+00B0) or the word :string:`degrees` is acceptable. Works that use both are normalized to use the dominant method.

Abbreviated units of temperature
================================

#.	Units of temperature measurement, like Farenheit or Celcius, may be abbreviated to :string:`F` or :string:`C`.

#.	Units of temperature measurement do not have trailing periods.

#.	If an *abbreviated* unit of temperature measurement is preceded by a number, the unit of measurement is first preceded by a hair space (:utf:` ` or U+200A).

#.	Abbreviated units of measurement are set in small caps.

#.	Abbreviated units of measurement are wrapped in an :html:`<abbr class="temperature">` element.

	.. code:: css

		abbr.temperature{
			font-variant: all-small-caps;
		}

	.. code:: html

		<p>It was −23.33° Celsius (or −10°:ws:`hairsp`<abbr class="temperature">F</abbr>) last night.</p>

Scansion
********

Scansion is the representation of the metrical stresses in lines of verse.

#.	:utf:`×` (U+00d7) indicates an unstressed sylllable and :utf:`/` (U+002f) indicates a stressed syllable. They are separated from each other with no-break spaces (U+00A0).

	.. code:: html

		<p>Several of his types, however, constantly occur; <abbr>e.g.</abbr> A and a variant (/ × | / ×) (/ × × | / ×); B and a variant (× / | × /) (× × / | × /); a variant of D (/ × | / × ×); E (/ × × | /). </p>

#.	Lines of poetry listed on a single line (like in a quotation) are separated by a space, then a forward slash, then a space. Capitalization is preserved for each line.

	.. code:: html

		<p>The famous lines “Wake! For the Sun, who scatter’d into flight / The Stars before him from the Field of Night” are from <i epub:type="se:name.publication.book">The Rubáiyát of Omar Khayyám</i>.</p>

Legal cases and terms
*********************

#.	Legal cases are set in italics.

#.	Either :string:`versus` or :string:`v.` are acceptable in the name of a legal case; if using :string:`v.`, a period follows the :string:`v.`, and it is wrapped in an :html:`<abbr>` element.

	.. code:: html

		<p>He prosecuted <i epub:type="se:name.legal-case">Johnson <abbr>v.</abbr> Smith</i>.</p>

Morse code
**********

Any Morse code that appears in a book is changed to fit Standard Ebooks’ format.

American Morse Code
===================

#.	Middle dot glyphs (:utf:`·` or U+00B7) are used for the short mark or dot.

#.	En dash (:utf:`–` or U+2013) are used for the longer mark or short dash.

#.	Em dashes (:utf:`—` or U+2014) are used for the long dash (the letter L).

#.	If two en dashes are placed next to each other, a hair space (:utf:` ` or U+200A) is placed between them to keep the glyphs from merging into a longer dash.

#.	Only in American Morse Code, there are internal gaps used between glyphs in the letters C, O, R, or Z. No-break spaces (U+00A0) are used for these gaps.

#.	En spaces (U+2002) are used between letters.

#.	Em spaces (U+2003) are used between words.

		.. class:: wrong

			.. code:: html

				<p>--  .. ..   __  ..  - -  __  .   . ..  __  -..   .. .  .- -</p>
				<p>My little old cat.</p>

		.. class:: corrected

			.. code:: html

				<p>– – ·· ·· — ·· – – — · · · — –·· ·· · ·– –</p>
				<p>My little old cat.</p>

Citations
*********

#.	Citations are wrapped in a :html:`<cite>` element.

#.	Citations that are the source of a quote are preceded by a space and an em dash, within the :html:`<cite>` element.

	.. code:: html

		<p>“The Moving Finger writes; and, having writ, moves on.” <cite>—<i epub:type="se:name.publication.book">The Rubaiyat of Omar Khayyam</i></cite>.</p>

#.	Citations within a :html:`<blockquote>` element have the :html:`<cite>` element as the last direct child of the :html:`<blockquote>` parent.

	.. class:: wrong

		.. code:: html

			<blockquote>
				<p>“The Moving Finger writes; and, having writ, moves on.”</p>
				<p>
					<cite>—<i epub:type="se:name.publication.book">The Rubaiyat of Omar Khayyam</i></cite>
				</p>
			</blockquote>

	.. class:: corrected

		.. code:: html

			<blockquote>
				<p>“The Moving Finger writes; and, having writ, moves on.”</p>
				<cite>—<i epub:type="se:name.publication.book">The Rubaiyat of Omar Khayyam</i></cite>
			</blockquote>

Verses and Chapters of the Bible
================================

#.	Citations of passages from the Bible include the name of the book, followed by the chapter number and the verse number. The chapter and the verse numbers are separated by a colon.

	#.	All chapter and verse numbers are written in Arabic numerals. Similarly, if a book being cited is a “numbered” book, the number is also written in Arabic numerals.

	.. class:: wrong

		.. code:: html

			<blockquote>
				<p>“Though I speak with the tongues of men and of angels, and have not charity, I am become as sounding brass, or a tinkling cymbal.”</p>
				<cite>—<span epub:type="z3998:roman">I</span> Corinthians <span epub:type="z3998:roman">XIII</span> 1</cite>
			</blockquote>

	.. class:: corrected

		.. code:: html

			<blockquote>
				<p>“Though I speak with the tongues of men and of angels, and have not charity, I am become as sounding brass, or a tinkling cymbal.”</p>
				<cite>—1 Corinthians 13:1</cite>
			</blockquote>

#.	If an entire chapter, instead of a particular verse, is being cited, then the citation includes the name of the book followed by the chapter number.

	.. class:: wrong

		.. code:: html

			<p>“In the beginning God created the heaven and the earth” is the first verse of Genesis <span epub:type="z3998:roman">I</span>.</p>

	.. class:: corrected

		.. code:: html

			<p>“In the beginning God created the heaven and the earth” is the first verse of Genesis 1.</p>

#.	If a continuous range of verses is being cited, an en-dash (:utf:`–` or U+2013) is placed between the verse numbers indicating the beginning and the end of the range.

	.. code:: html

		<p>Matthew 5:3–11.</p>

	Ranges may also span multiple chapters within the same book:

	.. code:: html

		<p>Matthew 5:1–7:29.</p>

#.	If a discontinuous group of verses in the same chapter is being cited, each distinct verse number is separated by a comma followed by a space.

	.. code:: html

		<p>Matthew 6:2, 16.</p>

#.	If there are multiple citations of the same book, each citation is separated by a semicolon followed by a space, and the name of the book is omitted after the first citation.

	.. code:: html

		<p>Matthew 5:3–11; 5:1–7:29; 6:2, 16</p>

Non-Latin Scripts and Transliterations
**************************************

#.	Greek script is set in italics. All other scripts are not set in italics unless specially required by the text.

Greek
=====

#.	Rough breathing marks are set using their precomposed character, if available; for example, :utf:`Ἁ`, :utf:`ἇ`, and :utf:`Ἧ`. If a precomposed character is not available, :utf:` ̔` (U+0314) is used when the mark must be combined with a character, and :utf:`ʽ` (U+02BD) is used in all other cases.

#.	Smooth breathing marks are set with :utf:`◌̓` (U+0313) when the mark must be combined with a character. :utf:`᾿` (U+1FBF) is used in all other cases.

Chinese
=======

#.	Wade-Giles is the preferred method of transliterating Chinese script. (`See here for discussion. <https://github.com/standardebooks/laozi_tao-te-ching_james-legge/issues/2>`__) Transliteration to Wade-Giles from Legge is permitted, but not required.

#.	In Wade-Giles transliteration, rough breathing marks are set using :utf:`ʽ` (U+02BD).
