#!/usr/bin/python3
def pow(a, b):
    ans = 1

    if b == 0:
        return (1)
    elif b > 0:
        for i in range(0, b):
            ans *= a
    else:
        b *= -1
        for i in range(0, b):
            ans *= a
        ans = 1 / ans

    return (ans)
