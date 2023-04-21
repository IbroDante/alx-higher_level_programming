#!/usr/bin/python3
""" Module that writes an Object to text file using
JSON representation
"""

import json


def save_to_json_file(my_obj, filename):
    """ Function that writes an object to text file
    JSON representation

    Args:
        my_obj: object
        filename: textfile name

    Raises:
        Exception: when the object can't encoded
    """

    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
