#!/usr/bin/env python3
'''Using Redis as a simple cache'''


import redis
from typing import Union
from uuid import uuid4


class Cache:
    """A class that Caches using Redis"""
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """stores and returns data"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key
