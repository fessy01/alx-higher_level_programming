#!/usr/bin/python3
"""A class Square that define a square"""


class Square:
    """Declearing class"""

    def __init__(self, size=0):
        """Initializing object/instance"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """eturning the square area of the object"""
        return (self.__size ** 2)

    @property
    def size(self):
        """ Method to returns the size value"""
        return self.__size

    @size.setter
    def size(self, value):
        """ Method to set the size value of the square object"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
