#!/usr/bin/python3
"""Defines square class."""


class Square:
    """represent a square."""

    def __init__(self, size=0):
        '''Initialize a square object.

        Args:
            size (int): size of the square object
        '''
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """compute & return the current area of a square object"""

        return self.__size ** 2
