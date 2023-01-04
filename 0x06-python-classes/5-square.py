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

    @property
    def size(self):
        '''retrieve size on a square object'''

        return self.__size

    @size.setter
    def size(self, value):
        '''set size of a square object'''

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """compute & return the current area of a square object"""

        return self.__size ** 2

    def my_print(self):
        '''print in stdout a square obj using the character #'''

        if self.__size == 0:
            print()
        else:
            for row in range(self.__size):
                for col in range(self.__size):
                    print("#", end='')
                print()
