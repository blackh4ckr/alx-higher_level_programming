#!/usr/bin/python3
import sys
if __name__ == '__main__':
    arguments = sys.argv[1:]
    int_args = [int(arg) for arg in arguments]
    print(sum(int_args))

