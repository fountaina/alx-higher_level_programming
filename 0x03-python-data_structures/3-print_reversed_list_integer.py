#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """ Prints the list of integers in reverse """
    if len(my_list) == 0:
        return (None)
    a = 1
    while a <= len(my_list):
        print('{:d}'.format(my_list[-a]))
        a += 1
