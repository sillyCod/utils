# -*- coding: utf-8 -*-
# @Time    : 2017/11/8 16:22
# @File    : decorator.py
import functools


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
            print symbol * size
            return func(*sub, **kwargs)

        return wrapper

    return wrap

