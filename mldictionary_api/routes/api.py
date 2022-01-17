from flask import Blueprint, jsonify, request
from werkzeug.exceptions import NotFound, InternalServerError

from api_dictionary.const import API_PREFIX, DICTIONARIES


dictionary = Blueprint('api_dictionary', __name__, url_prefix=API_PREFIX)


@dictionary.route('/dictionary/en/<word>/')
@dictionary.route('/dictionary/pt/<word>/')
@dictionary.route('/dictionary/es/<word>/')
@dictionary.route('/translator/en-pt/<word>/')
@dictionary.route('/translator/pt-en/<word>/')
def api(word: str):
    choice = request.url.split('/')[5]
    dictionary = DICTIONARIES[choice]

    if not (meanings := dictionary.get_meanings(word)):
        raise NotFound(f'"{word}" not found, check the spelling and try again')
    return jsonify({'source': dictionary.URL.format(word), 'meanings': meanings}), 200


@dictionary.errorhandler(NotFound)
def not_found(err):
    return jsonify({'message': err.description}), err.code


@dictionary.errorhandler(InternalServerError)
def internal_error(err):
    return jsonify({'message': err.description}), err.code


@dictionary.errorhandler(Exception)
def general_exception(err):
    return jsonify({'message': 'Don\'t recognize erro'}), 500
