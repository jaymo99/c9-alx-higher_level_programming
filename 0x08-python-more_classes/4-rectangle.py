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
        '''
        Return an informal string representation of rectangle object
        '''

        if self.__width > 0 and self.__height > 0:
            rect = []
            for h in range(self.__height):
                for w in range(self.__width):
                    rect.append("#")

                # print new line except for the last line
                if h < (self.__height - 1):
                    rect.append("\n")
            return ("".join(rect))
        else:
            return ("")

    def __repr__(self):
        '''
        Return a formal string representation of rectangle object
        '''

        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def area(self):
        '''computes area of a rectangle'''

        return (self.__width * self.__height)

    def perimeter(self):
        '''returns perimeter of a rectangle'''

        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
