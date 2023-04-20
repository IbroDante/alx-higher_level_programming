#!/usr/bin/python3

import json
import csv
import os.path


class Base:
    """
    Base class for managing id attribute in all future classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes an instance with an id attribute
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
