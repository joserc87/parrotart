from logging import getLogger

from flask import Blueprint

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
    pass
