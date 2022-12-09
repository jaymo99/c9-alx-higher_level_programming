#!/usr/bin/python3
if __name__ != "__main__":
    quit()

import sys

n = len(sys.argv)

print(f"{n - 1} arguments: " if n != 1 else f"{n - 1} argument: ")

for i in range(1, n):
    print(f"{i}: {sys.argv[i]}")
