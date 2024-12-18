#!/usr/bin/env python3
"""
redis exercise
"""
import redis
import random
from typing import Callable
from functools import wraps
from typing import Union
import uuid


def count_calls(method: Callable) -> Callable:
    """Decorator: counts the number of times a methods of the Cache class
    are called
    """
    key = method.__qualname__

    @wraps(method)
    def incr_calls(self, *args):
        self._redis.incr(key)
        return method(self, *args)

    return incr_calls


def call_history(method: Callable) -> Callable:
    """ Decorator: Stores history of inputs and outputs for a particular
    function.
    """
    input_list = method.__qualname__ + ":inputs"
    output_list = method.__qualname__ + ":outputs"

    @wraps(method)
    def add_to_input_list(self, *args):
        """Appends arguments to list"""
        self._redis.rpush(input_list, str(args))
        output = method(self, *args)
        self._redis.rpush(output_list, str(output))

    return add_to_input_list


class Cache:
    """
    Redis DB cache
    """

    def __init__(self):
        """initialise cache instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
