#!/usr/bin/python3
for i in range(0, 10):
    for k in range((i + 1), 10):
        if (i != 8) or (k != 9):
            print("{}{}, ".format(i, k), end="")
        else:
            print("{}{}".format(i, k))
