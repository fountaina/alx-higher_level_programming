#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """ Prints the list of integers in reverse """
    if len(my_list) == 0:
        return (None)
    my_list.reverse()
    for a in range(len(my_list)):
        print("{:d}".format(my_list[a]))
