#!/usr/bin/python3
"""Defines Square Class.

Classes:
    Square
"""


class Square:
    """Represents a square.

    Attributes:
        __size (int): size of square object
    """

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
