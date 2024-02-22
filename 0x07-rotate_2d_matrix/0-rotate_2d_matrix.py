#!/usr/bin/python3
"""
This module contains the rotate_2d_matrix function.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise
    """
    length = len(matrix)
    matrix_copy = [row[:] for row in matrix]
    for row in range(length):
        new_column = length - 1
        for column in range(length):
            matrix[row][column] = matrix_copy[new_column][row]
            new_column -= 1
