from flask import Flask

from mldictionary_api.routes import views, api


def create_app():
    app = Flask(__name__)

    app.register_blueprint(views)
    app.register_blueprint(api)

    return app
