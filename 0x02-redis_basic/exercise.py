#!/usr/bin/env python3
"""
redis exercise
"""
import redis
import random
from collections.abc import Callable
from functools import wraps
from typing import Union
import uuid


def count_calls(fn: Callable) -> Callable:
    """Decorator: counts the number of times a methods of the Cache class
    are called
    """
    key = fn.__qualname__

    @wraps(fn)
    def incr_calls(self, data):
        if self.get(key) is None:
            self._redis.set(key, 0)
        self._redis.incr(key)
        return fn(self, data)

    return incr_calls


class Cache:
    """
    Redis DB cache
    """

    def __init__(self):
        """initialise cache instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Takes an argument and returns a string
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None):
        """
        Returns data corresponding to the given key
        """
        data = self._redis.get(key)
        if data and fn:
            return fn(data)
        else:
            return data

    def get_str(self, data: bytes) -> str:
        """
        Parametrises Cache.get converts bytes to string
        """
        return data.decode('utf-8')

    def get_int(self, data: bytes) -> int:
        """
        Parametrises Cache.get, convert bytes to int
        """
        return int.from_bytes(data, 'big')
