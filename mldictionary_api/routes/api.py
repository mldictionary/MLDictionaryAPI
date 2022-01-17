import traceback

from flask import Blueprint, jsonify, request
from werkzeug.exceptions import NotFound, InternalServerError, TooManyRequests

from mldictionary_api.models import RedisRequests
from mldictionary_api.const import (
    API_PREFIX,
    DICTIONARIES,
    LOCAL_ADDR,
    TOTAL_REQUESTS_ALLOW,
    TTL_REQUEST,
)


api = Blueprint('mldictionary_api', __name__, url_prefix=API_PREFIX)


@api.route('/dictionary/en/<word>/')
@api.route('/dictionary/pt/<word>/')
@api.route('/dictionary/es/<word>/')
@api.route('/translator/en-pt/<word>/')
@api.route('/translator/pt-en/<word>/')
def dictionary(word: str):

    requests_db = RedisRequests()

    choice = request.url.split('/')[5]
    dictionary = DICTIONARIES[choice]
    request_ip = request.remote_addr
    total_requests = requests_db.get(f'requests:{request_ip}')
    if not (meanings := dictionary.get_meanings(word)):
        raise NotFound(f'"{word}" not found, check the spelling and try again')
    if request_ip != LOCAL_ADDR:
        if total_requests > TOTAL_REQUESTS_ALLOW:
            raise TooManyRequests(
                f'The address {request_ip} is allow to make only "{TOTAL_REQUESTS_ALLOW}" requests '
                f'wait until {int(TTL_REQUEST / 60)} minutes and try again'
            )

    requests_db.set(f'requests:{request_ip}', str(total_requests + 1), TTL_REQUEST)

    return jsonify({'source': dictionary.URL.format(word), 'meanings': meanings}), 200


@api.app_errorhandler(NotFound)
def not_found(err):
    traceback.print_tb(err.__traceback__)
    return jsonify({'message': err.description}), err.code


@api.app_errorhandler(TooManyRequests)
def too_many_requests(err):
    traceback.print_tb(err.__traceback__)
    return jsonify({'message': err.description}), err.code


@api.app_errorhandler(InternalServerError)
def internal_error(err):
    traceback.print_tb(err.__traceback__)
    return jsonify({'message': err.description}), err.code


@api.app_errorhandler(Exception)
def general_exception(err):
    traceback.print_tb(err.__traceback__)
    return jsonify({'message': 'Don\'t recognize erro'}), 500
