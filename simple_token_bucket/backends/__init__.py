from typing import Tuple


class Backend:
    def get_token(self, *, bucket_name: str, bucket_size: int, refresh_interval: int) -> Tuple[int, int]:
        """Returns available tokens in `bucket_name` and its time-to-live (
        number of seconds before the next refresh).

        Args:
            bucket_name: Bucket name.
            bucket_size: Default size of the bucket.
            refresh_interval: Bucket reset time interval (in seconds).

        Returns:
            2-element tuple containing:

            - **int**: number of tokens available.
            - **int**: nubmer of seconds before the next refresh.
        """
        raise NotImplementedError
