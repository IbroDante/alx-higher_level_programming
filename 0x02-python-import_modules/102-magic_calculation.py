#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for i in range(1, b+1):
        result += a ** i
    return result
