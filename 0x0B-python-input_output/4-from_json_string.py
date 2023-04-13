#!/usr/bin/python3
""" Module that contains function that returns object by
JSON representation
"""


import json


def from_json_string(my_str):
    """ Function that returns an object by a JSON representation

    Args:
        my_str: JSON representation

    Raises:
        Exception: when the string can't decoded

    """

    return json.loads(my_str)
