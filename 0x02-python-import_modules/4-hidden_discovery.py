#!/usr/bin/python3
if __name__ != "__main__":
    quit()

import hidden_4

for i in dir(hidden_4):
    if not (i[0] == '_' and i[1] == '_'):
        print(i)
