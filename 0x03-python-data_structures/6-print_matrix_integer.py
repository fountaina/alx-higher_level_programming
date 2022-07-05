#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return ('')
    for block in matrix:
        for idx in range(len(block)):
            if idx < (len(block) - 1):
                print('{}'.format(block[idx]), end=' ')
            else:
                print('{}'.format(block[idx]), end='')
        print(end='\n')
