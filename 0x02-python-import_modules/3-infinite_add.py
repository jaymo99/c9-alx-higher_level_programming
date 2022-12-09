#!/usr/bin/python3
if __name__ != "__main__":
    quit()

import sys

n = len(sys.argv)
s = 0

for i in range(1, n):
    s += int(sys.argv[i])
print("{}".format(s))
