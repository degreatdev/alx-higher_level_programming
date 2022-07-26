#!/usr/bin/python3
"""
    This module contains a function which add
    two integers, return the result and also
    raise exceptions.
"""


def add_integer(a, b=98):
    """
    add_integer - return the sum of two integers
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
