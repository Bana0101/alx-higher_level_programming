#!/usr/bin/python3
"""
Module documentation

this module provide a function for adding two integers
"""

import doctest


def add_integer(a, b=98):
    """
    A fucntion that add two integer
    """
    if not isinstance(a, float) and not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, float) and not isinstance(b, int):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

if __name__ == "__main__":
    doctest.testfile("tests/0-add_integer.txt")
