#!/usr/bin/python3
def lookup(obj):
    """ Function that return the list of the available attribute
        and method of object
    Arg:
        obj: instance of a class
    Return:
        List of an attribute
    """


    return dir(obj)
