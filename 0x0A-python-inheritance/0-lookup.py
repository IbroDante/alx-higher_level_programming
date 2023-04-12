#!/usr/bin/python3


def lookup(obj):
    return dir(obj)


class MyClass:
    def __init__(self):
        self.x = 1

    def my_method(self):
        pass


my_object = MyClass()
print(lookup(my_object))
