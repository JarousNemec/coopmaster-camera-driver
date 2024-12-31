from flask import Flask, send_file, Response
import requests
from io import BytesIO

from requests import Response
from requests.auth import HTTPDigestAuth

from flask import Blueprint, make_response

from app import configuration

camera_blueprint = Blueprint('camera_blueprint', __name__)


@camera_blueprint.route("/api/cam1/image", methods=['GET'])
def get_actual_image_cam1():
    camera_ip = configuration.config.CAM1_CAMERA_IP
    camera_user = configuration.config.CAM1_CAMERA_USERNAME
    camera_password = configuration.config.CAM1_CAMERA_PASSWORD
    return get_image(camera_ip, camera_user, camera_password)


@camera_blueprint.route("/api/cam2/image", methods=['GET'])
def get_actual_image_cam2():
    camera_ip = configuration.config.CAM2_CAMERA_IP
    camera_user = configuration.config.CAM2_CAMERA_USERNAME
    camera_password = configuration.config.CAM2_CAMERA_PASSWORD
    return get_image(camera_ip, camera_user, camera_password)


def get_image(camera_ip, user, password):

    # Camera configuration
    url = f'http://{camera_ip}/ISAPI/Streaming/channels/101/picture?videoResolutionWidth=1920&videoResolutionHeight=1080'

    try:
        # Fetch the image from the camera
        response = requests.get(url, auth=HTTPDigestAuth(user, password), stream=True)
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
