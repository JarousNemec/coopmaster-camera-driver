from flask import Flask
from config import Config

app = Flask('__main__')

@app.route("/")
def hello_world():
    return Config.hello_msg

def run():
    app.run(host="0.0.0.0", port=5000)
