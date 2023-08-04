__version__ = "0.1.2"


from .backends import Backend


class SimpleTokenBucket:
    def __init__(self, name: str, bucket_size: int, refresh_interval: int, backend: Backend):
        """Create a new SimpleTokenBucket.

        Every `refresh_interval` the token bucket is refresh and `bucket_size`
        tokens are available again.

        Args:
            name: Bucket name.
            bucket_size: Number of available tokens.
            refresh_interval: Bucket reset time interval (in seconds).
            backend: a :class:`.backends.Backend` implementation.
        """
        self.name = name
        self.bucket_size = bucket_size
        self.refresh_interval = refresh_interval
        self._backend = backend

    def try_get_token(self, raises=True) -> bool:
        available_tokens, ttl = self._backend.get_token(
            bucket_name=self.name,
            bucket_size=self.bucket_size,
            refresh_interval=self.refresh_interval,
        )

        if available_tokens <= 0:
            if raises:
                raise NotEnoughTokens(remaining_seconds=ttl)
            else:
                return False

        return True


class NotEnoughTokens(RuntimeError):
    def __init__(self, *, remaining_seconds: int):
        self.remaining_seconds = remaining_seconds

    def __str__(self):
        return f"NotEnoughTokens; {self.remaining_seconds} seconds until next reset"
