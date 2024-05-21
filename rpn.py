#!/usr/bin/env python

# Parse an RPN string, doing math.
# Assume the string is space-delimited, and only has the four +-*/ operators.
# Assume an operator only takes 2 numbers as arguments.

input = "242 233 / 23 +"

data = input.split()
stack = []

for token in data:
    if (token == "+") or (token == "-") or (token == "*") or (token == "/"):
        b = float(stack.pop())
        a = float(stack.pop())
        if token == "+":
            stack.append(a + b)
        if token == "*":
            stack.append(a * b)
        if token == "-":
            stack.append(a - b)
        if token == "/":
            stack.append(a / b)
    else:
        stack.append(float(token))
print(stack)
    
        

    
    

