from flask import Flask

from api_dictionary.routes import views, dictionary


def create_app():
    app = Flask(__name__)

    app.register_blueprint(views)
    app.register_blueprint(dictionary)

    return app
