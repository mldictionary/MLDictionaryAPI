from flask import Blueprint
from werkzeug.exceptions import NotFound, InternalServerError, TooManyRequests

from mldictionary_api.const import API_PREFIX
from mldictionary_api.resources.response import ResponseAPI
from mldictionary_api.resources.const import (
    ENGLISH_REPR,
    ENGLISH_TO_PORTUGUESE_REPR,
    PORTUGUESE_REPR,
    PORTUGUESE_TO_ENGLISH,
    SPANISH_REPR,
)

api = Blueprint('mldictionary_api', __name__, url_prefix=API_PREFIX)


@api.route('/dictionary/en/<word>/')
def english(word: str):
    return ResponseAPI().get_meanings(ENGLISH_REPR, word)


@api.route('/dictionary/pt/<word>/')
def portuguese(word: str):
    return ResponseAPI().get_meanings(PORTUGUESE_REPR, word)


@api.route('/dictionary/es/<word>/')
def spanish(word: str):
    return ResponseAPI().get_meanings(SPANISH_REPR, word)


@api.route('/translator/en-pt/<word>/')
def english_to_portuguese(word: str):
    return ResponseAPI().get_meanings(ENGLISH_TO_PORTUGUESE_REPR, word)


@api.route('/translator/pt-en/<word>/')
def portuguese_to_english(word: str):
    return ResponseAPI().get_meanings(PORTUGUESE_TO_ENGLISH, word)


@api.app_errorhandler(NotFound)
def not_found(err):
    return ResponseAPI().handle_error(err)


@api.app_errorhandler(TooManyRequests)
def too_many_requests(err):
    return ResponseAPI().handle_error(err)


@api.app_errorhandler(InternalServerError)
def internal_error(err):
    return ResponseAPI().handle_error(err)


@api.app_errorhandler(Exception)
def general_exception(err):
    err.description = 'Don\'t recognize erro'
    err.code = 500
    return ResponseAPI().handle_error(err)
