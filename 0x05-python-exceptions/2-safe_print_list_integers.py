#!/usr/bin/python3
def safe_print_list_integers(my_list=None, x=0):
    if my_list is None:
        my_list = []
    count = 0
    for i in my_list:
        if isinstance(i, int):
            print("{:d}".format(i), end="")
            count += 1
            if count == x:
                break
    print()
    return count
