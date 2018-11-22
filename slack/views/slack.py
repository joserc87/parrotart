from logging import getLogger

from flask import Blueprint, jsonify, request

from partyparrot import convert
from ..utils import parse_emojify_args

slack = Blueprint('slack', __name__)
logger = getLogger('slack')


@slack.route('/', methods=['GET'])
def slack_test():
    return 'Slack api is running'


@slack.route('/emojify', methods=['GET'])
def emojify_test():
    return 'Emojify uses POST'


@slack.route('/emojify', methods=['POST'])
def emojify():
    text = request.form['text']
    args = parse_emojify_args(text)
    message = args[0]
    fg = args[1] if len(args) > 1 else ':black_circle:'
    bg = args[2] if len(args) > 2 else ':white_circle:'
    text = convert(message, fg, bg)
    payload = {'text': text}
    return jsonify(payload)
