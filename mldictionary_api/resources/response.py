import traceback
from typing import Type

from flask import jsonify, request
from mldictionary import Dictionary
from werkzeug.exceptions import NotFound, TooManyRequests

from mldictionary_api.models import RedisRequests, RedisMeaningsCache
from mldictionary_api.resources.const import (
    DICTIONARIES,
    LIMITED_REQUESTS_DICTIONARIES,
    LIMITED_REQUESTS,
    TOTAL_REQUESTS_ALLOW,
    TTL_MEANINGS_CACHE,
    TTL_REQUEST,
)


class ResponseAPI:
    def get_meanings(self, lang: str, word: str):
        dictionary = DICTIONARIES[lang]
        request_ip = self.__get_request_ip(request.headers.getlist("X-Forwarded-For"))
        total_requests = RedisRequests().get(f'requests:{request_ip}')

        if limited_request := self.__limit_request(dictionary):
            if total_requests > TOTAL_REQUESTS_ALLOW:
                raise TooManyRequests(
                    f'The address {request_ip} is allow to make only "{TOTAL_REQUESTS_ALLOW}" requests '
                    f'wait until {int(TTL_REQUEST / 60)} minutes and try again'
                )

        if not (meanings := self.__get_meanings(word, dictionary)):
            self.__save_request_attempt(request_ip, total_requests, limited_request)
            raise NotFound(f'"{word}" not found, check the spelling and try again')

        self.__save_request_attempt(request_ip, total_requests, limited_request)
        self.__make_cache(dictionary.language.lower(), word, meanings, limited_request)

        return (
            jsonify({'source': dictionary.url.format(word), 'meanings': meanings}),
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

    def __limit_request(self, dictionary: Type[Dictionary]) -> bool:
        if not LIMITED_REQUESTS:
            return False

        for limited_dictionary in LIMITED_REQUESTS_DICTIONARIES:
            if isinstance(dictionary, limited_dictionary):
                return True
        return False

    def __get_meanings(self, word: str, dictionary: Type[Dictionary]) -> list[str]:
        meanings = RedisMeaningsCache().get(
            f'meanings:{dictionary.language.lower()}:{word.lower()}'
        )
        return meanings if meanings else dictionary.get_meanings(word)

    def __save_request_attempt(self, request_ip: str, total_requests: int, limited_request: bool):
            if limited_request:
                RedisRequests().set(
                    f'requests:{request_ip}',
                    str(total_requests + 1),
                    TTL_REQUEST
                )

    def __make_cache(self, dict_lan: str, word: str, meanings: list[str], limited_request: bool):
        if limited_request:
            RedisMeaningsCache().set(
                f'meanings:{dict_lan}:{word.lower()}', meanings, TTL_MEANINGS_CACHE
            )
