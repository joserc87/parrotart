from logging import getLogger

from flask import Blueprint, Flask

logger = getLogger('app')

HOST='127.0.0.1'
PORT='5000'
DEBUG=False

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)

    from slack.views.slack import slack
    app.register_blueprint(slack, url_prefix='/slack')

    return app

app = create_app('.config')


def main():
    logger.info("Starting Flask Server on http://{host}:{port}".format(host=HOST, port=PORT))
    app.run(debug=DEBUG, host=HOST, port=PORT)


if __name__ == "__main__":
    main()
