from partyparrot import convert_with_alphabet_emojis


def test_convert_char_to_alphabet():
    assert convert_with_alphabet_emojis("") == ""
    assert convert_with_alphabet_emojis(" ") == "   "
    assert convert_with_alphabet_emojis("\n") == "\n"
    assert (
        convert_with_alphabet_emojis(" one two")
        == "   :alphabet-white-o::alphabet-white-n::alphabet-white-e:   "
        ":alphabet-white-t::alphabet-white-w::alphabet-white-o:"
    )
    assert (
        convert_with_alphabet_emojis("1_'")
        == ":alphabet-white-question:"*3
    )
    assert (
        convert_with_alphabet_emojis("?!")
        == ":alphabet-white-question::alphabet-white-exclamation:"
    )
