#!/usr/bin/python3
if __name__ != "__main__":
    quit()

import sys

n = len(sys.argv)
args = n - 1

print(f"{args} arguments" if (args) != 1 else f"{args} argument", end='')
print(f":" if args > 0 else ".")

if n > 1:
    for i in range(1, n):
        print(f"{i}: {sys.argv[i]}")
