#!/usr/bin/python3
"""Defines square class."""


class Square:
    """represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        '''Initialize a square object.

        Args:
            size (int): size of the square object
            position (int, int): the position of the square object
        '''
        self.size = size
        self.position = position

    @property
    def size(self):
        '''set size of a square object'''

        return self.__size

    @size.setter
    def size(self, value):
        '''set size of a square object'''

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        '''get the position of a square object'''

        return self.__position

    @position.setter
    def position(self, value):
        '''set position of a square object'''

        if type(value) is not tuple or \
                len(value) != 2 or \
                not all(isinstance(num, int) for num in value) or \
                not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """compute & return the current area of a square object"""

        return self.__size ** 2

    def my_print(self):
        '''print in stdout a square obj using the character #'''

        if self.__size == 0:
            print()
        else:
            for y_axis in range(self.__position[1]):
                print()

            for row in range(self.__size):
                for col in range(self.__position[0]):
                    print(" ", end='')
                for col in range(self.__size):
                    print("#", end='')
                print()
