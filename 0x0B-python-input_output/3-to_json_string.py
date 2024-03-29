#!/usr/bin/python3
""" Module that contains a function that returns the JSON
representation object
"""
import json


def to_json_string(my_obj):
    """ Function that return the JSON representation object
    Args:
        my_obj: object
    Raises:
        Exception: when the object can't be encoded
    """

    return json.dumps(my_obj)
