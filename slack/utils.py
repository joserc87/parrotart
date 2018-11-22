import re


regex = r":[^:\s]*(?:::[^:\s]*)*:"


def parse_emojify_args(text):
    matches = re.finditer(regex, text)
    matches = list(matches)
    if len(matches) > 2:
        raise SyntaxError('Expected 2 emojis, at most')

    message = text
    if len(matches) > 0:
        message = text[:matches[0].start()]
        message = message.strip()

    output = [message] + [match.group() for match in matches]
    return output
