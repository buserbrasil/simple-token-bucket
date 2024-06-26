from unittest import mock

import fakeredis
import pytest

from simple_token_bucket import NotEnoughTokens, SimpleTokenBucket
from simple_token_bucket.backends.redis import RedisBackend


@pytest.fixture
def redis_client():
    return fakeredis.FakeStrictRedis(version=6)


def test_redis_backend_ok(redis_client):
    listener = mock.MagicMock()
    token_bucket = SimpleTokenBucket(
        name="test_ok",
        bucket_size=3,
        refresh_interval=60,
        backend=RedisBackend(redis_client),
        listener=listener,
    )
    assert token_bucket.try_get_token() is True
    listener.assert_called_once_with(3)


def test_redis_backend_not_enough_tokens_raises(redis_client):
    token_bucket = SimpleTokenBucket(
        name="test_not_enough_tokens",
        bucket_size=1,
        refresh_interval=60,
        backend=RedisBackend(redis_client),
    )
    assert token_bucket.try_get_token() is True

    with pytest.raises(NotEnoughTokens, match=r"NotEnoughTokens; \d+ seconds until next reset"):
        token_bucket.try_get_token()


def test_redis_backend_not_enough_tokens_not_raises(redis_client):
    token_bucket = SimpleTokenBucket(
        name="test_not_enough_tokens_not_raises",
        bucket_size=1,
        refresh_interval=60,
        backend=RedisBackend(redis_client),
    )
    assert token_bucket.try_get_token() is True
    assert token_bucket.try_get_token(raises=False) is False
