#!/usr/bin/python3
"""
contains MyList class
"""


class MyList(list):
    """ a suclass"""
    def __init__(self):
        """ initialize object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted"""
        new_list = MyList()
        for item in self:
            new_list.append(item)
        new_list.sort()
        print(new_list)
