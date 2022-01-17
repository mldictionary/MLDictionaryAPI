from random import randint as random
from datetime import datetime

from flask import Blueprint, render_template

from mldictionary_api.const import VIEWS_PREFIX, API_USE_EXAMPLES


views = Blueprint('views', import_name=__name__, url_prefix=VIEWS_PREFIX)


@views.route('/')
def index():
    arguments = {
        'version': '0.0.2',
        'example': API_USE_EXAMPLES[random(0, len(API_USE_EXAMPLES) - 1)],
        'warning': True,
        'year': datetime.now().year,
    }
    return render_template('index.jinja2', **arguments), 200
