#!/usr/bin/python3

def uppercase(str):
    for i in range(len(str)):
        if i < len(str) - 1:
            n = ord(str[i])
            if n > 90:
                n = n - 32
            else:
                n = n
            print("{}".format(chr(n)), end='')
        else:
            n = ord(str[len(str) - 1])
            if n > 90:
                n = n - 32
            else:
                n = n
            print("{}".format(chr(n)))
