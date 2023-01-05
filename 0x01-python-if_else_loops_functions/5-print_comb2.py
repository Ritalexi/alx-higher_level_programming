#!/usr/bin/python3
for i in range(0, 100):
    if (i <= 98):
        k = i // 10
        j = i % 10
        print("{0:d}{1}, ".format(k, j), end="")
    elif (i >= 99):
        print("{}".format(i))
