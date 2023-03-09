#!/usr/bin/python3
import sys
import calculator_1 as c1

if __name__ == '__main__':
    args = sys.argv[1:]
    nargs = len(args)

    if nargs != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)
    elif args[1] not in ['+', '-', '*', '/']:
        print('Unknown operator. Available operators: +, -, * and /')
        sys.exit(1)
    else:
        a = int(args[0])
        b = int(args[2])

        if args[1] == '+':
            print('{} + {} = {}'.format(a, b, c1.add(a, b)))
        elif args[1] == '-':
            print('{} - {} = {}'.format(a, b, c1.sub(a, b)))
        elif args[1] == '*':
            print('{} * {} = {}'.format(a, b, c1.mul(a, b)))
        elif args[1] == '/':
            print('{} / {} = {}'.format(a, b, c1.div(a, b)))

