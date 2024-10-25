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
            return fn(key)
        else:
            return data
    
    def get_str(self, ):
        """
        Parametrises Cache.get
        """
        

