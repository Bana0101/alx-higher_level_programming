#!/usr/bin/python3
""" module documentation"""


def print_square(size):
    """ a function that prints a square with the character #."""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size < 0 and isinstance(size, float):
        raise TypeError("size must be an integer")
    for _ in range(size):
        print("#" * size)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
