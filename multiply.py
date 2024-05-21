#!/usr/bin/env python

def multiply(list):
    acc = 1
    for num in list:
        acc *= num
    return acc

print(multiply([2, 3, 4, 5]))
print(multiply([]))
