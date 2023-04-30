#!/usr/bin/python3


def pascal_triangle(n):
    """ Function that prints the pascal triangle
    Args:
        n: number of lines
    """
    if n <= 0:
        return []

    matrix = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(matrix[i - 1][j - 1] + matrix[i - 1][j])
        row.append(1)
        matrix.append(row)

    for i in matrix:
        print(" ".join(str(j) for j in i))

    return matrix
