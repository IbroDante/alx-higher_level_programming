#!/usr/bin/python3
""" Module that create Object from JSON file
"""

import json

def load_from_json_file(filename):
    """ Function that create Object from JSON file
    
    Args:
        filename: textfile name
    
    Raises:
        Exception: when the object can't encoded
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.load(file)
