#!/usr/bin/python3
'''Module defines one class, 'Rectangle' '''


from .base import Base


class Rectangle(Base):
    '''
    This class represents a rectangle.

    It inherits from Base class and has additional attributes to
    represent the width and height of the rectangle

    It has an 'x' and 'y' attribute representing its position on
    a cartesian plane.
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        initialize a rectangle

        Args:
            width (int): width of the rectangle
            length (int): height of the rectangle
            x (int): x coordinate of the rectangle
            y (int): y coordinate of the rectangle
            id (int): unique identifier for the object
        '''

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return (self.__x)

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return (self.__y)

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''
        Returns the area value of the Rectangle instance
        '''

        return (self.width * self.height)

    def display(self):
        '''
        Print a Rectangle instance with the char '#'
        '''

        for h in range(self.height):
            for w in range(self.width):
                print("#", end='')
            print()
