#!/usr/bin/env python3
"""
redis exercise
"""
import redis
import random
from typing import Union
import uuid


class Cache:
    """
    Redis DB cache
    """

    def __init__(self):
        """initialise cache instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Takes an argument and returns a string
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn=None):
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

