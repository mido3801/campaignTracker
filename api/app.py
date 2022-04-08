from flask import Flask
from flask_cors import CORS
from flasgger import Swagger

from db import db
from config import env_config
from flask_jwt_extended import JWTManager
from datetime import timedelta
from resources import api


def create_app(config_name):
    """
    Application factory pattern
    :return: flask app object
    """
    app = Flask(__name__)
    app.config.from_object(env_config[config_name])
    app.config["JWT_SECRET_KEY"] = "please-remember-to-change-me"
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=1)

    # Initialize app extensions
    db.init_app(app)
    api.init_app(app)
    CORS(app)
    Swagger(app)
    JWTManager(app)

    return app


def deploy():
    """
    Run deployment tasks
    """
    app = create_app()
    app.app_context().push()

