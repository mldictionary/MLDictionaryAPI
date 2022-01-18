import traceback
from typing import Type

from flask import jsonify, request
from mldictionary import Dictionary
from werkzeug.exceptions import NotFound, TooManyRequests

from mldictionary_api.models import RedisRequests, RedisMeaningsCache
from mldictionary_api.resources.const import (
    DICTIONARIES,
    LIMITED_REQUESTS_DICTIONARIES,
    LOCAL_ADDR,
    TOTAL_REQUESTS_ALLOW,
    TTL_MEANINGS_CACHE,
    TTL_REQUEST,
)


class ResponseAPI:
    def get_meanings(self, lang, word):
        dictionary = DICTIONARIES[lang]
        request_ip = self.__get_request_ip(request.headers.getlist("X-Forwarded-For"))

        if not (ilimited_dictionary := self.__valid_request(request_ip, dictionary)):
            total_requests = RedisRequests().get(f'requests:{request_ip}')
            if total_requests > TOTAL_REQUESTS_ALLOW:
                raise TooManyRequests(
                    f'The address {request_ip} is allow to make only "{TOTAL_REQUESTS_ALLOW}" requests '
                    f'wait until {int(TTL_REQUEST / 60)} minutes and try again'
                )

        if not (meanings := self.__get_meanings(word, dictionary)):
            raise NotFound(f'"{word}" not found, check the spelling and try again')

        if not ilimited_dictionary:
            self.__make_cache(request_ip, total_requests, word, meanings)
        return (
            jsonify({'source': dictionary.URL.format(word), 'meanings': meanings}),
            200,
        )

    def handle_error(self, err):
        traceback.print_tb(err.__traceback__)
        return (
            jsonify({'message': err.description, 'http_status': err.code}),
            err.code,
        )

    def __get_request_ip(self, heroku_proxy_header: list[str]):
        return (
            request.remote_addr if not heroku_proxy_header else heroku_proxy_header[0]
        )

    def __valid_request(self, request_ip: str, dictionary: Type[Dictionary]):
        if request_ip in LOCAL_ADDR:
            return True

        for limited_dictionary in LIMITED_REQUESTS_DICTIONARIES:
            if isinstance(dictionary, limited_dictionary):
                return False
        return True

    def __get_meanings(self, word: str, dictionary: Type[Dictionary]) -> list[str]:
        meanings = RedisMeaningsCache().get(f'meanings:{word}')
        return meanings if meanings else dictionary.get_meanings(word)

    def __make_cache(
        self, request_ip: str, total_requests: int, word: str, meanings: list[str]
    ):

        RedisRequests().set(
            f'requests:{request_ip}', str(total_requests + 1), TTL_REQUEST
        )
        RedisMeaningsCache().set(f'meanings:{word}', meanings, TTL_MEANINGS_CACHE)
