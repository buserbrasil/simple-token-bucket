Simple Token Bucket
===================

Simple Token Bucket is meant to be a light and very simple to use
token bucket library. `Simple is better than
complex <https://peps.python.org/pep-0020/>`_.

Usage::

    from simple_token_bucket import SimpleTokenBucket
    from simple_token_bucket.backends.redis import RedisBackend

    third_party_api_rate_limit_bucket = SimpleTokenBucket(
        name="third_party_api",
        bucket_size=3,
        interval=10,
    )

    third_party_api_rate_limit_bucket.try_get_token()
    third_party_api_rate_limit_bucket.try_get_token()
    third_party_api_rate_limit_bucket.try_get_token()

    # will raises NotEnoughTokens
    third_party_api_rate_limit_bucket.try_get_token()

    # after 10 seconds everythin works again
    import time
    time.sleep(10)
    third_party_api_rate_limit_bucket.try_get_token()



Installation
------------

Simple Token Bucket requires Python 3.8 or newer to run.

.. code-block:: bash

   pip install simple_token_bucket[redis]


API Reference
-------------

.. toctree::
   :maxdepth: 3

   api


Additional Notes
----------------

.. toctree::
   :maxdepth: 1

   contributing


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
