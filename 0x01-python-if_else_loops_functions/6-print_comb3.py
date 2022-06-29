#!/usr/bin/python3
for n in range(10):
    for i in range(n+1, 10):
        if n < 8:
            print('{0}{1}, '.format(n, i), end='')
        elif n == 8:
            print('{0}{1}'.format(n, i), end='')
