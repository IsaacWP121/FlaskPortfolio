from flask import Flask
from flask_sqlalchemy import SQLalchemy
from os import path
from flask_login import LoginManager

def create_app():
	app = Flask(__name__)
	app.config["SECRET_KEY"] = "placeHolderKey"


	return app