#!/usr/bin/env python

# Merge two sorted lists into a new sorted list, without increasing memory usage.

A = [2, 4, 6, 8, 10, 234, 888, 900, 1096]
B = [1, 3, 5, 7, 9, 27, 99, 101, 900]
C = []

while (len(A) + len(B)) > 0:
    if len(A) > 0:
        a = A[0]
    else:
        C+=B
        break
    if len(B) > 0:
        b = B[0]
    else:
        C+=A
        break
    if (a <= b):
        A.pop(0)
        C.append(a)
    else:
        B.pop(0)
        C.append(b)

print("The merged list is ", C)
