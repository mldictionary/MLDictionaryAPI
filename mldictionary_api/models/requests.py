__all__ = ['RedisRequests']

from mldictionary_api.models.base import RedisBaseModel


class RedisRequests(RedisBaseModel):
    def __init__(self):
        super().__init__()

    def get(self, match: str) -> int:
        requests = self.db.get(match) or 0
        return int(requests)

    def set(self, key, value, ttl: int):
        self.db.set(key, value, ex=ttl)
