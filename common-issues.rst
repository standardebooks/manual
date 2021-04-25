##########
Common Issues Converting from PD Transcriptions/Scans
##########

Punctuation
***********
#. Punctuation, other than periods, appearing immediately inside a closing parenthesis should be moved outside the parenthesis.

    .. class:: wrong

	    .. code:: html

		    <p>…my brothers, (though fain would I see you all,) before my death…</p>

    .. class:: corrected

	    .. code:: html

		    <p>…my brothers, (though fain would I see you all), before my death…</p>

#. Place names, e.g. pubs, inns, etc., should have quote-marks removed.

    .. class:: wrong

	    .. code:: html

		    <p>“Shall we get supper at the ‘Lame Cow’?”</p>

    .. class:: corrected

	    .. code:: html

		    <p>“Shall we get supper at the Lame Cow?”</p>

Capitalization
**************
#. Lowercase words immediately following exclamations and question-marks was a common practice and should be left as is.

	.. code:: html

		<p>“Surrender you two! and confound you for two wild beasts!”</p>

#. Older PD works, especially eighteenth century and prior, often used uppercased words as a kind of emphasis. Unless they are for purposes of personification, they should be changed to lowercase.

    .. class:: wrong

    	.. code:: html

	    	<p>To the eye of History many things, in that sick-room of Louis, are now visible, which to the Courtiers there present were invisible.</p>

    .. class:: corrected

	    .. code:: html

		    <p>To the eye of History many things, in that sick-room of Louis, are now visible, which to the courtiers there present were invisible.</p>

Elision
*******
#. Semi-colons were occasionally used for elision in names; these should be replaced with the SE standard two-em dash for partial elision, three-em dash for full elision.

    .. class:: wrong

	    .. code:: html

		    <p>When I turned myself over to a Letter from a Beneficed Clergyman in the Country to the Bishop of C…r, I was becoming languid…"</p>

    .. class:: corrected

	    .. code:: html

		    <p>When I turned myself over to a Letter from a Beneficed Clergyman in the Country to the Bishop of C⸺r, I was becoming languid…"</p>


Diacritics
**********
#. Diacritics on words that appear in Merriam-Webster without them should be removed. Modernize spelling corrects some of these, so it is best to wait until after that step to see if any others are left. :bash:`se find-mismatched-diacritics` can help find instances of these.

    .. class:: wrong

	    .. code:: html

		    <p>“Is not that the hôtel in which is enclosed the garden of the Lingère du Louvre?”

    .. class:: corrected

	    .. code:: html

		    <p>“Is not that the hotel in which is enclosed the garden of the Lingère du Louvre?”

Headers
*******
#. Periods that appear after the chapter number or title should be removed.

    .. class:: wrong

	    .. code:: html

    		<h2 epub:type="title"></h2>

    .. class:: corrected

	    .. code:: html

		    <h2 epub:type="title"></h2>

Italics
*******
#. If italicized non-English words are found in Merriam-Webster, the italics should be removed.

    .. class:: wrong

	    .. code:: html

		    <p>“No, you certainly have not, old man,” put in Rogers <i>sotto voce</i>.</p>

    .. class:: corrected

	    .. code:: html

		    <p>“No, you certainly have not, old man,” put in Rogers sotto voce.</p>


#. Words and/or phrases that are italicized in the source, or italicized and quoted, should be changed to match SE standards. For example, it may be italicized in the source, but should be quoted according to our style manual. Or, an English phrase may be quoted and italicized, and only one is necessary (usually the quotes).

    .. class:: wrong

	    .. code:: html

		    <p></p>

    .. class:: corrected

	    .. code:: html

		    <p></p>

