from logging import getLogger

from flask import Blueprint, jsonify, request

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
    payload = {'text': 'Echo:' + text}
    return jsonify(payload)
