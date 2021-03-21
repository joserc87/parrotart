from slack.views.slack import do_emojify


class TestEmojify:
    def test_do_emojify_empty(self):
        assert do_emojify("") == ""

    def test_do_emojify_no_icons(self):
        assert do_emojify("Hello world!") == (
            ":alphabet-white-h::alphabet-white-e::alphabet-white-l:"
            ":alphabet-white-l::alphabet-white-o:   :alphabet-white-w:"
            ":alphabet-white-o::alphabet-white-r::alphabet-white-l:"
            ":alphabet-white-d::alphabet-white-exclamation:"
        )

    def test_do_emojify_wrong_format(self):
        assert do_emojify(":icon: Hello world!") == "\n\n\n\n"

    def test_do_emojify_foreground_icon(self):
        assert do_emojify("Hello world! :icon:") == (
            ":icon::nbsp::nbsp::icon::nbsp::icon::icon::icon::icon::nbsp::icon::nbsp::nbsp::nbsp::nbsp::icon::nbsp::nbsp::nbsp::nbsp::nbsp::icon::icon::nbsp::nbsp::nbsp::nbsp::nbsp::icon::nbsp::nbsp::nbsp::icon::nbsp::nbsp::icon::icon::nbsp::nbsp::icon::icon::icon::nbsp::nbsp::icon::nbsp::nbsp::nbsp::nbsp::icon::icon::icon::nbsp::nbsp::icon::icon::icon:\n"
            ":icon::nbsp::nbsp::icon::nbsp::icon::nbsp::nbsp::nbsp::nbsp::icon::nbsp::nbsp::nbsp::nbsp::icon::nbsp::nbsp::nbsp::nbsp::icon::nbsp::nbsp::icon::nbsp::nbsp::nbsp::nbsp::icon::nbsp::nbsp::nbsp::icon::nbsp::icon::nbsp::nbsp::icon::nbsp::icon::nbsp::nbsp::icon::nbsp::icon::nbsp::nbsp::nbsp::nbsp::icon::nbsp::nbsp::icon::nbsp::nbsp::nbsp::icon:\n"
            ":icon::icon::icon::icon::nbsp::icon::icon::icon::nbsp::nbsp::icon::nbsp::nbsp::nbsp::nbsp::icon::nbsp::nbsp::nbsp::nbsp::icon::nbsp::nbsp::icon::nbsp::nbsp::nbsp::nbsp::icon::nbsp::icon::nbsp::icon::nbsp::icon::nbsp::nbsp::icon::nbsp::icon::icon::icon::nbsp::nbsp::icon::nbsp::nbsp::nbsp::nbsp::icon::nbsp::nbsp::icon::nbsp::nbsp::icon:\n"
            ":icon::nbsp::nbsp::icon::nbsp::icon::nbsp::nbsp::nbsp::nbsp::icon::nbsp::nbsp::nbsp::nbsp::icon::nbsp::nbsp::nbsp::nbsp::icon::nbsp::nbsp::icon::nbsp::nbsp::nbsp::nbsp::icon::nbsp::icon::nbsp::icon::nbsp::icon::nbsp::nbsp::icon::nbsp::icon::nbsp::nbsp::icon::nbsp::icon::nbsp::nbsp::nbsp::nbsp::icon::nbsp::nbsp::icon:\n"
            ":icon::nbsp::nbsp::icon::nbsp::icon::icon::icon::icon::nbsp::icon::icon::icon::icon::nbsp::icon::icon::icon::icon::nbsp::nbsp::icon::icon::nbsp::nbsp::nbsp::nbsp::nbsp::nbsp::icon::nbsp::icon::nbsp::nbsp::nbsp::icon::icon::nbsp::nbsp::icon::nbsp::nbsp::icon::nbsp::icon::icon::icon::icon::nbsp::icon::icon::icon::nbsp::nbsp::nbsp::icon:"
        )
