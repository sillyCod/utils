# -*- coding: utf-8 -*-
# @Time    : 2017/11/8 16:22
# @File    : decorator.py
import functools
from simplejson import JSONDecodeError


def debug_decorator(symbol, size):
    """
    Silly function to make debug more simple.
    :param symbol:
    :param size:
    :return:
    """
    def wrap(func):
        @functools.wraps(func)
        def wrapper(*sub, **kwargs):
            if not (isinstance(symbol, str) and isinstance(size, int)):
                raise TypeError("Please make sure the symbol str and size int")
            print(symbol * size)
            return func(*sub, **kwargs)

        return wrapper

    return wrap


def json_decr(**kwwargs):
    """
    decorator for dealing with JsonDecodeError.
    :param kwwargs:
    :return:
    """
    default = kwwargs.pop('default', {})

    def wrapper(func):
        @functools.wraps(func)
        def wrap(*sub, **kwargs):
            try:
                ret = func(*sub, **kwargs)
            except JSONDecodeError as e:
                print(e.message)
                return default
            else:
                return ret
        return wrap
    return wrapper


def ret_verify():
    pass
