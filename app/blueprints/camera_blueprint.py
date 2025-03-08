import logging

from flask import Flask, send_file, Response
import requests
from io import BytesIO

from requests import Response
from requests.auth import HTTPDigestAuth

from flask import Blueprint, make_response

from app import configuration

camera_blueprint = Blueprint('camera_blueprint', __name__)


@camera_blueprint.route("/api/dog/image", methods=['GET'])
def get_actual_image_dog():
    camera_ip = configuration.config.DOG_CAMERA_IP
    camera_user = configuration.config.DOG_CAMERA_USERNAME
    camera_password = configuration.config.DOG_CAMERA_PASSWORD
    logging.info(f"Getting image from dog camera: {camera_ip}")
    return get_image(camera_ip, camera_user, camera_password)


@camera_blueprint.route("/api/chicken/image", methods=['GET'])
def get_actual_image_chicken():
    camera_ip = configuration.config.CHICKEN_CAMERA_IP
    camera_user = configuration.config.CHICKEN_CAMERA_USERNAME
    camera_password = configuration.config.CHICKEN_CAMERA_PASSWORD
    logging.info(f"Getting image from chicken camera: {camera_ip}")
    return get_image(camera_ip, camera_user, camera_password)


def get_image(camera_ip, user, password):

    # Camera configuration
    url = f'http://{camera_ip}/ISAPI/Streaming/channels/101/picture?videoResolutionWidth=1920&videoResolutionHeight=1080'

    try:
        # Fetch the image from the camera
        response = requests.get(url, auth= (user, password), stream=True)
        response.raise_for_status()  # Raise an error for bad responses

        # Read the image into memory
        img_stream = BytesIO(response.content)

        # Send the image as a response
        return send_file(img_stream, mimetype='image/jpeg')

    except requests.exceptions.RequestException as e:
        # Handle errors and send an appropriate response
        print(f"Error fetching image: {e}")
        return Response(status=500, response=str(e))
    return make_response(response)
