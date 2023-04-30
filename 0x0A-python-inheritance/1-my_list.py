#!/usr/bin/python3
"""
contains MyList class
"""


class MyList(list):
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        new_list = MyList()
        for item in self:
            new_list.append(item)
        new_list.sort()
        print(new_list)
