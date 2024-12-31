from flask import Blueprint, make_response



admin_blueprint = Blueprint('admin_blueprint', __name__)



@admin_blueprint.route("/api/ping", methods=['GET'])
def ping():
    response = {"ping": "pong"}
    return make_response(response)
