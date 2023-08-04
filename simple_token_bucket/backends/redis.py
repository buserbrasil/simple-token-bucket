from typing import Tuple
from . import Backend
import redis


class RedisBackend(Backend):
    @classmethod
    def from_url(cls, redis_url: str):
        client = redis.StrictRedis.from_url(redis_url)
        return RedisBackend(client)

    def __init__(self, redis_client: redis.Redis):
        self._client = redis_client

    def get_token(self, *, bucket_name: str, bucket_size: int, refresh_interval: int) -> Tuple[int, int]:
        pipeline = self._client.pipeline()
        pipeline.set(bucket_name, bucket_size, nx=True, ex=refresh_interval)
        pipeline.ttl(bucket_name)
        pipeline.get(bucket_name)
        pipeline.decr(bucket_name)
        _, ttl, available_tokens, _ = pipeline.execute()

        if ttl < 0:
            return int(bucket_size), refresh_interval
        return int(available_tokens), ttl
