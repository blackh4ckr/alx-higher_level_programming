#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for x in range(len(my_list)):
        my_list = sorted(my_list, reverse=True)
        print('{:d}'.format(my_list[x]))
