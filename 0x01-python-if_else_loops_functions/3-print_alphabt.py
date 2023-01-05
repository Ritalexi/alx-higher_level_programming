#!/usr/bin/python3
y = ''
for x in range(97, 123):
    y += chr(x)
    print(y[0:4] + y[5:16] + y[17:26], end="")
