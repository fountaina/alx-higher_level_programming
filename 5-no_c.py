#!/usr/python3
def no_c(my_string):
    i = 0
    for a in my_string:
        if a == 'c' or a == 'C':
            i+=1
            continue
        else:
            print(a, end='')
            i+=1
