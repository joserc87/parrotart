#!/usr/bin/env python

import sys

letters = {'a': ['0110', '1001', '1001', '1111', '1001'],
           'b': ['1110', '1001', '1110', '1001', '1110'],
           'c': ['0110', '1001', '1000', '1001', '0110'],
           'd': ['1110', '1001', '1001', '1001', '1110'],
           'e': ['1111', '1000', '1110', '1000', '1111'],
           'f': ['1111', '1000', '1110', '1000', '1000'],
           'g': ['0110', '1000', '1011', '1001', '0110'],
           'h': ['1001', '1001', '1111', '1001', '1001'],
           'i': ['111', '010', '010', '010', '111'],
           'j': ['0011', '0001', '0001', '1001', '0110'],
           'k': ['1001', '1010', '1100', '1010', '1001'],
           'l': ['1000', '1000', '1000', '1000', '1111'],
           'm': ['10001', '11011', '10101', '10001', '10001'],
           'n': ['1001', '1101', '1011', '1001', '1001'],
           'o': ['0110', '1001', '1001', '1001', '0110'],
           'p': ['1110', '1001', '1110', '1000', '1000'],
           'q': ['01100', '10010', '10010', '10010', '01111'],
           'r': ['1110', '1001', '1110', '1001', '1001'],
           's': ['0111', '1000', '0110', '0001', '1110'],
           't': ['11111', '00100', '00100', '00100', '00100'],
           'u': ['1001', '1001', '1001', '1001', '0110'],
           'v': ['1001', '1001', '1001', '1010', '0100'],
           'w': ['10001', '10001', '10101', '10101', '01010'],
           'x': ['1001', '1101', '0110', '1011', '1001'],
           'y': ['1001', '1001', '1110', '0010', '0100'],
           'z': ['1111', '0001', '0110', '1000', '1111'],
           ' ': ['00', '00', '00', '00', '00'],
           '?': ['1110', '0010', '0100', '0000', '0100'],
           }


def get_letter(letter):
    return letters[letter] if letter in letters else letters['?']


def convert(text, foreground_emoji=':partyparrot:',
            background_emoji=':invisibleparrot:'):
    sprites = [get_letter(c) for c in text.lower()]
    rows = ['0'.join(x[i] for x in sprites) for i in range(5)]
    rows = [r[:r.rfind('1') + 1] for r in rows]
    base = '\n'.join(rows)

    base = base.replace('0', background_emoji)
    base = base.replace('1', foreground_emoji)

    return base


special_alphabet_char = {
    '?': 'question',
    '!': 'exclamation',
}


def valid_alphabet_char(char):
    i = ord(char)
    return char in special_alphabet_char or i >= ord('a') and i <= ord('z')

def convert_char_to_alphabet(char):
    char = char.lower()

    if char == ' ':
        return '   '
    elif char == '\n':
        return '\n'

    if not valid_alphabet_char(char):
        char = '?'
    char = special_alphabet_char.get(char, char)
    return f':alphabet-white-{char}:'


def convert_with_alphabet_emojis(text):
    return ''.join(convert_char_to_alphabet(c) for c in text)


def main():
    if len(sys.argv) <= 1:
        print('''Missing text
Usage:
    partyparrot.py text [foreground_emoji] [background_emoji]
''')
    else:
        text = sys.argv[1]
        args = {}
        if len(sys.argv) >= 3:
            args['foreground_emoji'] = sys.argv[2]
        if len(sys.argv) == 4:
            args['background_emoji'] = sys.argv[3]
        print(convert(text, **args))

if __name__ == '__main__':
    main()
