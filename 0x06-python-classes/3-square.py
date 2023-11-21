#!/usr/bin/python3
"""Square."""


class Square:
    """Defines a square."""
    def __init__(self, size=0):
        """
        initialize a new instance
        Attribute:
        - size (int): the size of the square
        """
        # size must be an integer
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        # size must be positive
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    # returns the current square area
    def area(self):
        return self.__size ** 2
