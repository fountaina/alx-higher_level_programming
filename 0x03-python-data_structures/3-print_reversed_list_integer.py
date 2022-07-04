#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    a = 1
    while a <= len(my_list):
        print('{0}'.format(my_list[-a]), end='\n')
        a+=1
