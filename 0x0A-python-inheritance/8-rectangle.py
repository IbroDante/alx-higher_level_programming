#!/usr/bin/python3
"""define class rectangle iherits from basegeo"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class that defines a rectangle from basegeo """

    def __init__(self, width, height):
        """ Initializes instance """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
