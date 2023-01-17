#!/usr/bin/python3
'''This module defines a Base class'''


class Base:
    '''
    This class is the 'base' of other classes in this project.

    It manages an 'id' attribute in all derived classes
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        '''
        initialize the object's id.

        Args:
            id (int): integer value for id
        '''

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
