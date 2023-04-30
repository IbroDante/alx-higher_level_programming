#!/usr/bin/python3
""" Module that executes a func appends"""


def append_after(filename="", search_string="", new_string=""):
    """ Func that appends a new line when a string is found
    Args:
        filename: filename
        search_string: string to search
        new_string: string to append
    """
    lines = []
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)

    with open(filename, 'w', encoding="utf-8") as f:
        f.writelines(lines)
