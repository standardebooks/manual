# Purpose and voice

The Standard Ebooks Manual of Style describes a complete approach to editing and producing ebooks, from internal code style to semantic enhancement and typography rules.

It is not a how-to manual; that is, it does not aim to give instructions on how to accomplish the various goals it describes. For example, it would not contain step by step guides, or guides on Inkscape usage, or SE toolset usage. Instead, the manual describes in declarative language how a Standard Ebook should appear after it is produced.

Each directive is numbered and can contain any number of sub directives. Directives declare what the expected final appearance *is*, not how a producer *should achieve the final appearance*.

For example:

Good: `“OK” is set without periods or spaces.`

Bad: `Don’t put periods or spaces in “OK”` or `“OK” shouldn’t be set with periods or spaces.`

# Submitting changes

The `master` branch is reserved for typo fixes, clarifications, and version releases. Anything else should be committed to the `next` branch, which is periodically merged into `master` as a version release.

# Building

The following `pip` packages are required:

```shell
pip3 install beautifulsoup4 pygments natsort regex rst2html5
```

To build the final PHP files, invoke the `build-manual.py` executable:

```shell
./build-manual.py SOURCE_DIR DEST_DIR
```

To generate the syntax highlighting stylesheet:

```shell
pygmentize -S monokai -f html > monokai.css
```

# Versioning

The overall version of the manual is stored as a comment in the `index.rst` file. This comment is used by `build-manual.py` to set the version number of the manual.

Within `.rst` files, the string `VERSION` is replaced with the version number when built. For example, a link to another part of the manual could be: `` `The SE identifier </manual/VERSION/9-metadata#9.2>`__ ``.

# Code style

## Indentation

All indentation is with tabs, not spaces.

A tab space follows the bullet point in all list items:

```rst
-	List item 1

-	List item 2

#.	List item 1

#.	List item 2
```

## RST extensions

Several additional RST roles are available for use in the manual:

- HTML: `` :html:`<p>Some HTML</p>` ``

- CSS: `` :css:`.some-class{ font-weight: bold; }` ``

- Bash: `` :bash:`se build --check .` ``

- Paths: `` :path:`/standardebooks.org/web/www/` ``

- Italics (`<i>`, not `<em>`): `` :italics:`The Iliad` ``

- Whitespace: `` :ws:`hairsp` ``

- UTF: `` :utf:`½` ``

- HTML attribute value: `` :value:`A value of an HTML attribute` ``

- String: `` :string:`A string that is not syntax highlighted` ``

While they are not defined in each `.rst` file to avoid header clutter, they are defined by `build-manual.py` during the build process.

You may also create a tip or warning block:

```rst
.. tip::

	Here’s a tip!

.. warning::

	Here’s a warning!
```

The string `PD_YEAR` will be replaced with `<?= PD_YEAR ?>`, which will print the current public domain year when served from the SE website. For example, it will print `1926` if the current public domain includes works published up to and including 1926.

The string `PD_STRING` will be replaced with `<?= PD_STRING ?>`, which will print the first day the public domain ends when served from the SE website. For example, it will print `January 1, 1927` if the current public domain includes works published up to and including 1926.

## Headings

```rst
####
<h1>
####

<h2>
****

<h3>
====

<h4>
----

<h5>
~~~~

<h6>
^^^^
```

## Numbered directives

All headings are automatically numbered and begin new `<section>` elements.

Numbered directives begin with `#.	` (Read: Hash, Period, Tab space) and begin new `<ol>` elements.

```rst
#.	Major structural divisions of a larger work, like parts, volumes, books, chapters, or subchapters, are contained in a :html:`<section>` element.

#.	Individual items in a larger collection (like a poem in a poetry collection) are contained in a :html:`<article>` element.
```

Sub-directives follow that convention, on the next indent level.

```rst
#.	:html:`<img>` elements have an :html:`alt` attribute that uses prose to describe the image in detail; this is what screen reading software will read aloud.

	#.	The :html:`alt` attribute describes the visual image itself in words, which is not the same as writing a caption or describing its place in the book.
```

To create a heading that is not numbered, precede it with the `..no-numbering` class:

```rst
.. class:: no-numbering

Examples
--------

Consider a book that contains several top-level subdivisions: Books 1–4, with each book having 3 parts, and each part having 10 chapters. Below is an example of three files demonstrating the structure necessary to achieve recomposability:
```

## Code samples

Block-level code samples are marked with the `.. code:: html` class:

```rst
.. code:: html

	<img alt="Pierre’s fruit-filled dinner" src="..." />
```

To add the “green check” or “red x” styling, add the `.. corrected` or `.. wrong` class:

```rst
.. class:: wrong

	.. code:: html

		<img alt="The illustration for chapter 10" src="..." />

.. class:: wrong

	.. code:: html

		<img alt="Pierre’s fruit-filled dinner" src="..." />
```
