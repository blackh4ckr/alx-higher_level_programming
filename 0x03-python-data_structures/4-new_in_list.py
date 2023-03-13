#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx not in range(len(my_list)):
        return my_list
    else:
        new_my_list = my_list[:]
        new_my_list[idx] = element
        return new_my_list
