#!/usr/bin/python3
"""defines """


def print_square(size):
    """ Function that prints a square with the character #
    Args:
        size: size of the square printed
    Returns:
        No return
    Raises:
        TypeError: If size is not an integer number
    """
    try:
        if isinstance(size, int):
            if size >= 0:
                for i in range(size):
                    print("#" * size)
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
    except Exception as e:
        print(e)
