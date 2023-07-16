# Simple Token Bucket

[![Documentation](https://readthedocs.org/projects/simple-token-bucket/badge/)](https://simple-token-bucket.readthedocs.io/en/latest/)
[![PyPI](https://img.shields.io/pypi/v/simple-token-bucket)](https://pypi.org/project/simple-token-bucket/)
![GitHub](https://img.shields.io/github/license/buserbrasil/simple-token-bucket)

A *simple* token bucket implementation.

## Project philosophy

`simple-token-bucket` is meant to be a light and very simple to use
token bucket library. [Simple is better than
complex](https://peps.python.org/pep-0020/).

## Installation

`simple-token-bucket` is available on PyPI:

```
python -m pip install simple-token-bucket[redis]
```

This project requires Python 3.8 or newer to run.

## Usage example

```python
from simple_token_bucket import SimpleTokenBucket
from simple_token_bucket.backends.redis import RedisBackend

# Create a new bucket
third_party_api_rate_limit_bucket = SimpleTokenBucket(
    name="third_party_api",
    bucket_size=3,
    interval=10,
    backend=RedisBackend.from_url("redis://localhost:6379/0")
)

third_party_api_rate_limit_bucket.try_get_token()
third_party_api_rate_limit_bucket.try_get_token()
third_party_api_rate_limit_bucket.try_get_token()

# will raises a NotEnoughTokens exception.
third_party_api_rate_limit_bucket.try_get_token()

# after 10 seconds everything works again.
import time
time.sleep(10)
third_party_api_rate_limit_bucket.try_get_token()
```

The latest documentation can be found here

> https://simple-token-bucket.readthedocs.io/en/latest/

## Contributing

Contributions are welcome. See Contributing section in docs.

