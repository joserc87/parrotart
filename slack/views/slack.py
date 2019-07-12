from logging import getLogger, FileHandler, DEBUG, Formatter

from flask import Blueprint, jsonify, request

from partyparrot import convert
from ..utils import parse_emojify_args

slack = Blueprint('slack', __name__)

logger = getLogger('slack')
logger.setLevel(DEBUG)
file_handler = FileHandler('app.log')
file_handler.setLevel(DEBUG)
formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

DEFAULT_FG_EMOJI = ':partyparrot:'
DEFAULT_BG_EMOJI = ':nbsp:'

@slack.route('/', methods=['GET'])
def slack_test():
    return 'Slack api is running'


@slack.route('/emojify', methods=['GET'])
def emojify_test():
    return 'Emojify uses POST'


@slack.route('/emojify', methods=['POST'])
def emojify():
    text = request.form['text']
    user_name = request.form['user_name']
    logger.debug(f'user {user_name} emojified {text}')
    args = parse_emojify_args(text)
    message = args[0]
    fg = args[1] if len(args) > 1 else DEFAULT_FG_EMOJI
    bg = args[2] if len(args) > 2 else DEFAULT_BG_EMOJI
    text = convert(message, fg, bg)
    payload = {'text': text}
    return jsonify(payload)
