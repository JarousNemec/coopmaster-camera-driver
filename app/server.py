import logging

from flask import Flask
from config import Config
from waitress import serve

def flask_app():
    app = Flask('__main__')

    @app.route("/")
    def hello_world():
        logging.info("Hello World!")
        return Config.hello_msg

    return app

def server(host: str = None, port: int = None, ssl: bool = False):
    manager_app = flask_app()

    logging.info("Serving on http://127.0.0.1:9001")
    serve(manager_app,  port=9001)