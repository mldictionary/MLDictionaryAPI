from flask import Flask

from api_dictionary.ext import views
from api_dictionary.ext import api

def create_app():
    app = Flask(__name__)
    views.init_app(app)
    api.init_app(app)
    return app