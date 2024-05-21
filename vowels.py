#!/usr/bin/env python

# Given a string, remove all the vowels. Handle non-alphabetic chars too.

def devowel(input):
    output = list(input)
    for v in ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U"):
        while v in output:
            output.remove(v)
    newstr = ""
    for e in output:
        newstr += e
    return newstr

print(devowel("hello world! this is -super- cool + woot woot"))

