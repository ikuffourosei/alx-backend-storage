#!/usr/bin/env python3
'''Using Redis as a simple cache'''


import redis
from typing import Union, Callable
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

    def get(self,
            key: str,
            fn: Callable = None) -> Union[str, bytes, int, float]:
        """Get the value of the given key
        Returns ('Nil') if None
        """
        data = self._redis.get(key)
        return data if fn is None else fn(data)

    def get_str(self, key: str) -> str:
        """Converts data to string"""
        return self._redis.get(key, lambda val: val.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """Returns redis information converted to int"""
        return self._redis.get(key, lambda val: int(val))
