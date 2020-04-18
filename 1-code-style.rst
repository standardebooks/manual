##############################
XHTML, CSS, and SVG Code Style
##############################

The :bash:`se clean` tool in the `Standard Ebooks toolset <https://standardebooks.org/tools>`__ formats XML, XHTML, CSS, and SVG code according to our style guidelines. The vast majority of the time its output is correct and no further modifications to code style are necessary.

XHTML formatting
****************

#.	The first line of all XHTML files is:

	.. code:: html

		<?xml version="1.0" encoding="utf-8"?>

#.	The second line of all XHTML files is (replace :html:`xml:lang="en-US"` with the `appropriate language tag <https://en.wikipedia.org/wiki/IETF_language_tag>`__ for the file):

	.. code:: html

		<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" epub:prefix="z3998: http://www.daisy.org/z3998/2012/vocab/structure/, se: https://standardebooks.org/vocab/1.0" xml:lang="en-US">

#.	Tabs are used for indentation.

#.	Tag names are lowercase.

#.	Elements whose content is `phrasing content <https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Content_categories#Phrasing_content>`__ are on a single line, with no whitespace between the opening and closing tags and the content.

	.. class:: wrong

		.. code:: html

			<p>
				It was a dark and stormy night...
			</p>

	.. class:: corrected

		.. code:: html

			<p>It was a dark and stormy night...</p>

:html:`<br/>` elements
======================

#.	:html:`<br/>` elements within `phrasing content <https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Content_categories#Phrasing_content>`__ are on the same line as the preceding phrasing content, and are followed by a newline.

	.. class:: wrong

		.. code:: html

			<p>“Pray for the soul of the
			<br/>
			Demoiselle Jeanne D’Ys.</p>

	.. class:: wrong

		.. code:: html

			<p>“Pray for the soul of the
			<br/>Demoiselle Jeanne D’Ys.</p>

	.. class:: corrected

		.. code:: html

			<p>“Pray for the soul of the<br/>
			Demoiselle Jeanne D’Ys.</p>

#.	The next indentation level after a :html:`<br/>` element is the same as the previous indentation level.

	.. class:: wrong

		.. code:: html

			<p>“Pray for the soul of the<br/>
				Demoiselle Jeanne D’Ys,<br/>
				who died<br/>
				in her youth for love of<br/>
				Philip, a Stranger.</p>

	.. class:: corrected

		.. code:: html

			<p>“Pray for the soul of the<br/>
			Demoiselle Jeanne D’Ys,<br/>
			who died<br/>
			in her youth for love of<br/>
			Philip, a Stranger.</p>

#.	The closing tag of the phrasing content broken by a :html:`<br/>` element is on the same line as the last line of the phrasing content.

	.. class:: wrong

		.. code:: html

			<p>“Pray for the soul of the<br/>
			Demoiselle Jeanne D’Ys.
			</p>

	.. class:: corrected

		.. code:: html

			<p>“Pray for the soul of the<br/>
			Demoiselle Jeanne D’Ys.</p>

#.	:html:`<br/>` elements have phrasing content both before and after; they don’t appear with phrasing content only before, or only after.

	.. class:: wrong

		.. code:: html

			<p>“Pray for the soul of the<br/>
			Demoiselle Jeanne D’Ys<br/></p>

	.. class:: corrected

		.. code:: html

			<p>“Pray for the soul of the<br/>
			Demoiselle Jeanne D’Ys</p>

Attributes
==========

#.	Attributes are in alphabetical order.

#.	Attributes, their namespaces, and their values are lowercase, except for values which are IETF language tags. In IETF language tags, the language subtag is capitalized.

	.. class:: wrong

		.. code:: html

			<section EPUB:TYPE="CHAPTER" XML:LANG="EN-US">...</section>

	.. class:: corrected

		.. code:: html

			<section epub:type="chapter" xml:lang="en-US">...</section>

#.	The string :string:`utf-8` is lowercase.

Classes
-------

#.	Classes are not used as one-time style hooks. There is almost always a clever selector that can be constructed instead of taking the shortcut of adding a class to an element.

#.	Classes are named semantically, describing *what they are styling* instead of the *resulting visual style*.

	.. class:: wrong

		.. code:: html

			<p>There was one great tomb more lordly than all the rest; huge it was, and nobly proportioned. On it was but one word</p>
			<blockquote class="small-caps">
				<p>Dracula.</p>
			</blockquote>

	.. class:: corrected

		.. code:: html

			<p>There was one great tomb more lordly than all the rest; huge it was, and nobly proportioned. On it was but one word</p>
			<blockquote class="tomb">
				<p>Dracula.</p>
			</blockquote>

CSS formatting
**************

#.	The first two lines of all CSS files are:

	.. code:: css

		@charset "utf-8";
		@namespace epub "http://www.idpf.org/2007/ops";

#.	Tabs are used for indentation.

#.	Selectors, properties, and values are lowercase.

Selectors
=========

#.	Selectors are each on their own line, directly followed by a comma or a brace with no whitespace in between.

	.. class:: wrong

		.. code:: css

			abbr.era, .signature{
				font-variant: all-small-caps;
			}


	.. class:: corrected

		.. code:: css

			abbr.era,
			.signature{
				font-variant: all-small-caps;
			}

#.	Complete selectors are separated by exactly one blank line.

	.. class:: wrong

		.. code:: css

			abbr.era{
				font-variant: all-small-caps;
			}


			strong{
				font-weight: normal;
				font-variant: small-caps;
			}

	.. class:: corrected

		.. code:: css

			abbr.era{
				font-variant: all-small-caps;
			}

			strong{
				font-weight: normal;
				font-variant: small-caps;
			}

#.	Closing braces are on their own line.

Properties
==========

#.	Properties are each on their own line (even if the selector only has one property) and indented with a single tab.

	.. class:: wrong

		.. code:: css

			abbr.era{ font-variant: all-small-caps; }

	.. class:: corrected

		.. code:: css

			abbr.era{
				font-variant: all-small-caps;
			}

#.	*Where possible*, properties are in alphabetical order.

	This isn’t always possible if a property is attempting to override a previous property in the same selector, and in some other cases.

#.	Properties are directly followed by a colon, then a single space, then the property value.

	.. class:: wrong

		.. code:: css

			blockquote{
				margin-left:	1em;
				margin-right:	1em;
				border:none;
			}

	.. class:: corrected

		.. code:: css

			blockquote{
				margin-left: 1em;
				margin-right: 1em;
				border: none;
			}

#.	Property values are directly followed by a semicolon, even if it’s the last value in a selector.

	.. class:: wrong

		.. code:: css

			abbr.era{
				font-variant: all-small-caps
			}

	.. class:: corrected

		.. code:: css

			abbr.era{
				font-variant: all-small-caps;
			}

SVG Formatting
**************

#.	SVG formatting follows the same directives as `XHTML formatting </manual/VERSION/1-code-style#1.1>`__.

Commits and Commit Messages
***************************

#.	Commits are broken into single units of work. A single unit of work may be, for example, "fixing typos across 10 files", or "adding cover art", or "working on metadata".

#.	Commits that introduce material changes to the ebook text (for example modernizing spelling or fixing a probable printer’s typo; but not fixing a transcriber’s typo) are prefaced with the string :string:`[Editorial]`, followed by a space, then the commit message. This makes it easy to search the repo history for commits that make editorial changes to the work.
