#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if i < j:
            print('{}{}'.format(i, j), end='')
            if '{}{}'.format(i, j) != '89':
                print(', ', end='')
print('')
