#!/usr/bin/python3
"""an empty classe"""


class Rectangle:
    """
    a class that define a Rectangle
    Attributes:
        width (float): the width of the rectangle
        height (float): the height of the rectangle
    """
    def __init__(self, width=0, height=0):
        """
        initializes a new instance of the Rectangle class
        Args:
            width (float): the width of the rectangle
            height (float): the height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        str_rect = ""
        for n in range(self.height):
            if n != self.height - 1:
                str_rect += "#" * self.width + "\n"
            else:
                str_rect += "#" * self.width
        return str_rect

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")
