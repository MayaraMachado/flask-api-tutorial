"""Flask Application"""

# load libaries
import sys
from flask import Flask, jsonify


# from yourapplication.model import db


def create_app(env='dev'):
    app = Flask(__name__)
    # app.config.from_object(env)

    # db.init_app(app)

    return app

