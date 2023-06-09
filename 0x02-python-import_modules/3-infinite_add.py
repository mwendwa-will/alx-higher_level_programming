#!/usr/bin/python3
def add_arg(argv):
    n = len(argv) - 1
    add = 0
    if n >= 1:
        i = 1
        add = 0
        while i <= n:
            add += int(argv[i])
            i += 1
    print("{:d}".format(add))


if __name__ == "__main__":
    import sys
    add_arg(sys.argv)
