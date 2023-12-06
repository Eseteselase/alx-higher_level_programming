#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        m_row = []
        for element in row:
            m_element = element ** 2
            m_row.append(m_element)
        new_matrix.append(m_row)
    return new_matrix
