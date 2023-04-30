#!/usr/bin/python3
""" defines int add func"""


def add_integer(a, b=98):
    """
    Adds two numbers and returns the result as an integer.
    
    Arguments:
        a (int/float): The first number to add.
        b (int/float, optional): The second number to add. Defaults to 98.
    
    Raises:
        TypeError: If either a or b is not an int or float.
    
    Returns:
        int: The result of adding a and b as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    
    return int(a) + int(b)
