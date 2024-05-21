#!/usr/bin/env python

# Sort a list of tuple-pairs by the 2nd element in each pair.
# Assume each pair contains integers.

def pairsort(input):
    answer = []
    dict = {}
    for tuple in input:
        dict[tuple[1]] = tuple
    keys = list(dict.keys())
    keys.sort()
    for key in keys:
        answer.append(dict[key])
    return answer

input = [(3,2), (9,1), (7,7), (4,5), (6,3)]
print(pairsort(input))
