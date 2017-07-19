#!/usr/bin/env python3
#-*- coding:UTF-8 -*-


import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# instantiate db
db = SQLAlchemy()


def create_app():
    # instantiate app
    app = Flask(__name__)

    # set config
    app_settings = os.environ.get("APP_SETTINGS")
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)

    # register blueprints
    from dashboard.api.views import users_blueprint
    app.register_blueprint(users_blueprint)

    return app

