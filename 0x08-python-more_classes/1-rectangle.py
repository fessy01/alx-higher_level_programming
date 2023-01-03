#!/usr/bin/python3
""" This is module that consist the class of a rectangle"""


class Rectangle:
    """ This is a class that define a rectangle"""
    def __init__(self, width=0, height=0):
        """Initializing the instance"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Method of returning the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Method that define width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Method of returning the value of height"""
        return self.__height

    @height.setter
    def width(self, value):
        """ Method that define height"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value
