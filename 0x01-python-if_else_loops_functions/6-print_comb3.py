#!/usr/bin/python3
for i in range(0, 8):
    for j in range(i + 1, 10):
        k = "{0}{1}".format(i, j)
        print(k, end=", ")
print("{0}{1}".format(i + 1, j))
