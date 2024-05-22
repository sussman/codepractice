#!/usr/bin/env python

# Given a string, output a compressed form that shows frequency of letters.
# e.g. "feeeedddmmee" --> "f4e3d2m2e"

def compress_string(s):
    prev = None
    output = ""
    count = 0
    for i in range(len(s)):
        if (s[i] != prev) and (prev != None):
            if (count == 1):
                output += prev
            else:
                output += str(count)
                output += prev
            count = 1
            prev = s[i]
        else:
            count += 1
            prev = s[i]
    
    if (count == 1):
        output += prev
    else:
        output += str(count)
        output += prev
    return output

print(compress_string("feeeedddmmee"))
