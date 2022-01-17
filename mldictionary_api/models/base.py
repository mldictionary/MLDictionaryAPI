from abc import abstractmethod

import redis

from mldictionary_api.models.const import (
    REDIS_HOST,
    REDIS_PORT,
    REDIS_USER,
    REDIS_PASSWORD,
)


class RedisBaseModel:
    def __init__(self):
        self.db = redis.StrictRedis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            username=REDIS_USER,
            password=REDIS_PASSWORD,
            db=0,
            charset='UTF-8',
            decode_responses=True,
        )

    @abstractmethod
    def get(self, match: str):
        ...

    @abstractmethod
    def set(self, key, value, ttl: int):
        ...
