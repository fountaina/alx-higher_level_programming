#!/usr/bin/python3


def no_c(my_string):
    """ returns a new string with all the c and C's removed """
    new_string = ""
    for i in range(len(my_string)):
        if my_string[i] != 'c' and my_string[i] != 'C':
            new_string += my_string[i]
    return (new_string)
