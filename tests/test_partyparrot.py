from partyparrot import convert_with_alphabet_emojis, convert


def test_convert_char_to_alphabet():
    assert convert_with_alphabet_emojis("") == ""
    assert convert_with_alphabet_emojis(" ") == "   "
    assert convert_with_alphabet_emojis("\n") == "\n"
    assert (
        convert_with_alphabet_emojis(" one two")
        == "   :alphabet-white-o::alphabet-white-n::alphabet-white-e:   "
        ":alphabet-white-t::alphabet-white-w::alphabet-white-o:"
    )
    assert convert_with_alphabet_emojis("1_'") == ":alphabet-white-question:" * 3
    assert (
        convert_with_alphabet_emojis("?!")
        == ":alphabet-white-question::alphabet-white-exclamation:"
    )


def test_convert():
    assert (
        convert("Hello world", ":icon:", ":nbsp")
        == ":icon::nbsp:nbsp:icon::nbsp:icon::icon::icon::icon::nbsp:icon::nbsp:nbsp:nbsp:nbsp:icon::nbsp:nbsp:nbsp:nbsp:nbsp:icon::icon::nbsp:nbsp:nbsp:nbsp:nbsp:icon::nbsp:nbsp:nbsp:icon::nbsp:nbsp:icon::icon::nbsp:nbsp:icon::icon::icon::nbsp:nbsp:icon::nbsp:nbsp:nbsp:nbsp:icon::icon::icon:\n:icon::nbsp:nbsp:icon::nbsp:icon::nbsp:nbsp:nbsp:nbsp:icon::nbsp:nbsp:nbsp:nbsp:icon::nbsp:nbsp:nbsp:nbsp:icon::nbsp:nbsp:icon::nbsp:nbsp:nbsp:nbsp:icon::nbsp:nbsp:nbsp:icon::nbsp:icon::nbsp:nbsp:icon::nbsp:icon::nbsp:nbsp:icon::nbsp:icon::nbsp:nbsp:nbsp:nbsp:icon::nbsp:nbsp:icon:\n:icon::icon::icon::icon::nbsp:icon::icon::icon::nbsp:nbsp:icon::nbsp:nbsp:nbsp:nbsp:icon::nbsp:nbsp:nbsp:nbsp:icon::nbsp:nbsp:icon::nbsp:nbsp:nbsp:nbsp:icon::nbsp:icon::nbsp:icon::nbsp:icon::nbsp:nbsp:icon::nbsp:icon::icon::icon::nbsp:nbsp:icon::nbsp:nbsp:nbsp:nbsp:icon::nbsp:nbsp:icon:\n:icon::nbsp:nbsp:icon::nbsp:icon::nbsp:nbsp:nbsp:nbsp:icon::nbsp:nbsp:nbsp:nbsp:icon::nbsp:nbsp:nbsp:nbsp:icon::nbsp:nbsp:icon::nbsp:nbsp:nbsp:nbsp:icon::nbsp:icon::nbsp:icon::nbsp:icon::nbsp:nbsp:icon::nbsp:icon::nbsp:nbsp:icon::nbsp:icon::nbsp:nbsp:nbsp:nbsp:icon::nbsp:nbsp:icon:\n:icon::nbsp:nbsp:icon::nbsp:icon::icon::icon::icon::nbsp:icon::icon::icon::icon::nbsp:icon::icon::icon::icon::nbsp:nbsp:icon::icon::nbsp:nbsp:nbsp:nbsp:nbsp:nbsp:icon::nbsp:icon::nbsp:nbsp:nbsp:icon::icon::nbsp:nbsp:icon::nbsp:nbsp:icon::nbsp:icon::icon::icon::icon::nbsp:icon::icon::icon:"
    )


def test_convert_wrong_char():
    txt = convert("@!*", ":icon:", ":nbsp")
    assert (
        txt
        == ":icon::icon::icon::nbsp:nbsp:icon::icon::icon::nbsp:nbsp:icon::icon::icon:\n:nbsp:nbsp:icon::nbsp:nbsp:nbsp:nbsp:icon::nbsp:nbsp:nbsp:nbsp:icon:\n:nbsp:icon::nbsp:nbsp:nbsp:nbsp:icon::nbsp:nbsp:nbsp:nbsp:icon:\n\n:nbsp:icon::nbsp:nbsp:nbsp:nbsp:icon::nbsp:nbsp:nbsp:nbsp:icon:"
    )
