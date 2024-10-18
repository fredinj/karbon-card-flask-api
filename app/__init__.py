from flask import Flask
from .routes.main import main_routes
from .routes.api import api

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Register the blueprint
    app.register_blueprint(main_routes)
    app.register_blueprint(api)

    return app