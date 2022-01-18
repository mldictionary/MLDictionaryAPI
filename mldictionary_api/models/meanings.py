__all__ = ['RedisMeaningsCache']

from mldictionary_api.models.base import RedisBaseModel


class RedisMeaningsCache(RedisBaseModel):
    def __init__(self):
        super().__init__()

    def get(self, match: str) -> list:
        meanings = self.db.smembers(match) or set()
        return list(meanings)

    def set(self, key, values, ttl: int):
        self.db.sadd(key, *values)
        self.db.expire(key, ttl)
