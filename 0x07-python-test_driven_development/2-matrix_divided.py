#!/usr/bin/python3
"""defines matrix division function"""


def matrix_divided(matrix, div):
    """
    This function divides the integer/float numbers of a matrix by a given number.

    Args:
        matrix (list): A list of lists of integers/floats.
        div (int/float): The number which divides the matrix.

    Returns:
        A new matrix with the result of the division.

    Raises:
        TypeError: If matrix or any of its elements is not a list of integers/floats.
                   If div is not an integer/float number.
        ZeroDivisionError: If div is zero.
        ValueError: If rows of the matrix have different lengths.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
