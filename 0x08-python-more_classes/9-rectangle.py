#!/usr/bin/python3
'''Defines a rectangle class'''


class Rectangle:
    '''Represents a rectangle'''

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        ''' Initializes a rectangle and increments the counter '''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
                    rect.append(str(self.print_symbol))

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

    def __del__(self):
        ''' Executed when a rectangle object is deleted '''

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def area(self):
        '''computes area of a rectangle'''

        return (self.__width * self.__height)

    def perimeter(self):
        '''returns perimeter of a rectangle'''

        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        ''' returns the biggest rectangle based on area'''

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_2.area()) > (rect_1.area()):
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        '''
        Returns a new rectangle instance
        with: width == height == size
        '''
        return Rectangle(size, size)
