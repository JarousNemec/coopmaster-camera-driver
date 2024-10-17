from flask import Flask
from config import Config

app = Flask(__name__)

@app.route("/")
def hello_world():
    return Config.hello_msg