#!/usr/bin/python3
from sys import argv

def argument():
    argv_len = len(argv[1:])
    print(argv_len)
    for i in range (1, argv_len + 1):
        print(f"{argv[i]}")
if __name__ == "__main__":
    argument()
