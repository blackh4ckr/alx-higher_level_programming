#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        max_value = 0
        for val in my_list:
            if val > max_value:
                max_value = val
        return max_value
