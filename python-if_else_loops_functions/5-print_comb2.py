#!/usr/bin/python3
for k in range(00, 100):
    if k < 99:
        print("{:02d},".format(k), end=" ")
    if k == 99:
        print("{:02d}".format(k), end="")
