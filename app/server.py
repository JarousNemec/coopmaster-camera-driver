import logging
from flask import Flask, send_file, Response
import requests
from io import BytesIO

from requests import Response
from requests.auth import HTTPDigestAuth
from waitress import serve

from app import configuration
from app.blueprints.admin_blueprint import admin_blueprint
from app.blueprints.camera_blueprint import camera_blueprint


def flask_app():
    app = Flask('__main__')

    @app.route("/")
    def hello_world():
        message = "Hello from camera gobbler"
        logging.info(message)
        return message

    app.register_blueprint(camera_blueprint)
    app.register_blueprint(admin_blueprint)



    return app


def server():
    manager_app = flask_app()
    host = configuration.config.HOST
    port = configuration.config.PORT
    logging.info(f"Serving on http://{host}:{port}/api/cam1/image")
    logging.info(f"Serving on http://{host}:{port}/api/cam2/image")
    serve(manager_app,  port=port)