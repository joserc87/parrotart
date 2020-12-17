from slack.utils import parse_emojify_args


class TestParseEmojifyArgs:
    def test_parsing_only_text(self):
        assert parse_emojify_args("Hello world!") == ["Hello world!"]

    def test_parsing_fg_emoji(self):
        assert parse_emojify_args("I love emojis :partyparrot:") == [
            "I love emojis",
            ":partyparrot:",
        ]

    def test_parsing_fg_and_bg_emoji(self):
        assert parse_emojify_args("I love emojis! :love: and :b:") == [
            "I love emojis!",
            ":love:",
            ":b:",
        ]
