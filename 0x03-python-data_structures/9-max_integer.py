#!/usr/bin/python3


def max_integer(my_list=[]):
    """Finds the biggest number in a list"""
    if len(my_list) == 0:
        return (None)

    biggest_integer = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > biggest_integer:
            biggest_integer = my_list[i]
    return (biggest_integer)
