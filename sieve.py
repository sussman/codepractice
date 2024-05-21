#!/usr/bin/env python

# Given a range of numbers [x,y], return all prime numbers in the range
# (Eratosthenes' sieve)

def return_primes(r):
    x = []
    for i in range(r[0], r[1]):
        x.append(i)
    s = range(2, int(r[1]/2))
    for e in s:
        newx = x.copy()
        for num in x:
            if ((num % e) ==  0) and (num != e):
                newx.remove(num)
        x = newx
    return x

print(return_primes([20,57]))


