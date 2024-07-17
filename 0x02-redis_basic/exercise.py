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

    def store(self, data: Union[bytes, str, int, float]) -> str:
        """
        Takes an argument and returns a string
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
