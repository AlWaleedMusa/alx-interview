#!/usr/bin/python3
"""
rotate matrix
"""


def rotate_2d_matrix(matrix):
    """
    rotate a matrix 90 degree clock wise
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()
