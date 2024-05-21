#!/usr/bin/env python

#  Given a string s, find the length of the longest substring without repeating characters.

def get_substring(s):

    seen = {} # have we ever seen the character before?
    count = 0 # current length of current unique substring (so far)
    count_record = 0 # length of longest unique substring we've ever seen

    for e in s:
        if e in seen:
            count = 0
        else:
            seen[e] = 1
            count += 1
            count_record += 1

    return count_record

print(get_substring("abcabcbb"))
print(get_substring("bbbbb"))
print(get_substring("pwwkew"))


