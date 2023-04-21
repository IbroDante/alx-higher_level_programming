#!/usr/bin/python3
def lookup(obj):
    """ Function that return the list of the available attribute
        and method of object
    Args:
        obj: instance of a class
    Returns:
        List of an attribute
    """


    return dir(obj)
