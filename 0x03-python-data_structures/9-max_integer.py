#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    biggest_integer = 0
    for integer in my_list:
        if integer > biggest_integer:
            biggest_integer = integer
    return (biggest_integer)