#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == None:
        return ('')
    for block in matrix:
        idx = 0
        for integer in block:
            if idx < (len(block) - 1):
                print('{}'.format(integer), end=' ')
                idx+=1
            else:
                print('{}'.format(integer), end='')
        print(end='\n')
