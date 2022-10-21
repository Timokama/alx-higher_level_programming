#!/usr/bin/python3
def matrix_divided(matrix, div):
    if not isinstance(div, (float, int)) or div != div:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if type(matrix) is not list:
        raise TypeError('matrix must be a matrix (list of lists) '
                'of integers/floats')
    types_row = map(lambda x: isinstance(x, list), matrix)
    if not all(types_row):
        raise TypeError('matrix must be a matrix (list of lists) '
                'of integers/floats')
    for row in matrix:
        types_elements = map(lambda x: isinstance(x,(float, int)), row)
        if not all(types_elements):
            raise TypeError('matrix must be a matrix (list of lists) '
                    'of integers/floats')
    for row in matrix:
        types_element = map(lambda x: x == x
                and x != float('inf')
                and x != -float('inf'),
                row)
        if not all(types_element):
            raise OverflowError
    size = map(lambda x: len(x) == len(matrix[0]), matrix)
    if not all(size):
        raise TypeError('Each row of the matrix must have the same size')

    mat_div = list(map(lambda x:
                        list(map(lambda y:
                            round(y / div, 2), x)), matrix))
    return mat_div

