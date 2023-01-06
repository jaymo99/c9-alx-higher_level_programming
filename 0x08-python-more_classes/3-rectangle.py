#!/usr/bin/python3
'''Defines a rectangle class'''


class Rectangle:
    '''Represents a rectangle'''

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
        else:
            raise TypeError("height must be an integer")

    def __str__(self):
        '''String representation of rectangle object'''

        if self.__width >= 0 and self.height >= 0:
            for h in range(self.__height):
                for w in range(self.__width):
                    print("#", end='')
                print()
        return ("")

    def area(self):
        '''computes area of a rectangle'''

        return (self.__width * self.__height)

    def perimeter(self):
        '''returns perimeter of a rectangle'''

        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
