from flask import Flask, current_app

from config import config


def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    config[config_name].init_app(app)

    # add blueprint
    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint)

    return app

