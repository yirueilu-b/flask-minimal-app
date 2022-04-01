from flask import Flask

my_app = Flask(__name__)


@my_app.route("/")
def hello_world():
    return "<p>Hello, Flask APP on Heroku!</p>"
