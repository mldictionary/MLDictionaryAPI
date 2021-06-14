from sys import version
from flask import Flask, render_template
from random import randint as random

def init_app(app: Flask)->None:
    
    @app.route('/')
    @app.route('/index.html')
    def index():
        routes_examples = [
            'v1/dictionary/en/',
            'v1/translator/en-pt/'
            ]
        examples = [
            routes_examples[random(0, 1)] + 'example',
            routes_examples[random(0, 1)] + 'current',
            routes_examples[random(0, 1)] + 'store',
            routes_examples[random(0, 1)] + 'life',
            routes_examples[random(0, 1)] + 'programming',
            routes_examples[random(0, 1)] + 'get',
            routes_examples[random(0, 1)] + 's',
            routes_examples[random(0, 1)] + 'sadness',
            routes_examples[random(0, 1)] + 'crazy',
            routes_examples[random(0, 1)] + 'mad'
            ]
        arguments = {
            'version': '0.0.1',
            'example': examples[random(0, len(examples)-1)],
            'warning': True
        }
        return render_template('index.html', **arguments)
