#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    flag_list = []
    for element in my_list:
        if element % 2 == 0:
            flag_list.append(True)
        else:
            flag_list.append(False)
    return (flag_list)
