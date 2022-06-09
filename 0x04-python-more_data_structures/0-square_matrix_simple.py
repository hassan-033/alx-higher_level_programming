#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    row = []
    for i in matrix:
        for j in i:
            row.append(j * j)
        new_matrix.append(row)
        row = []
    return new_matrix
