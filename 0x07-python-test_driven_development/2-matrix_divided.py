#!/usr/bin/python3
"""documentation module"""


def matrix_divided(matrix, div):
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    size = len(matrix[0])
    new_matrix = [row.copy() for row in matrix]
    for i in range(len(matrix)):
        if size != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(len(matrix[i])):
            new_matrix[i][j] = round(new_matrix[i][j] / div, 2)
    return new_matrix
