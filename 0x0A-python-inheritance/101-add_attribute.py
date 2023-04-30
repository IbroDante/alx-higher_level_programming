#!/usr/bin/python3
"""defines a func that adds attributes to objects."""


def add_attribute(obj, att, value):
     """ Func that adds a new attribute to an object
    Args:
        obj: object
        name: attribute name
        value: attribute value
    Raises:
        TypeError: when the attribute can't be added
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
