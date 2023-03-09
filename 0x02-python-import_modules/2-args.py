#!/usr/bin/python3
import sys

if __name__ == '__main__':
    args = sys.argv[1:]
    nargs = len(args)

    if nargs == 0:
        print('{} arguments.'.format(nargs))
    elif nargs == 1:
        print('{} argument: '.format(nargs))
        print('1: {}'.format(args[0]))
    else:
        print('{} arguments: '.format(nargs))
        for i in range(nargs):
            print('{}: {}'.format(i+1, args[i]))
