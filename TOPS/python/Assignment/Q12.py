"""
 Write a Python program to sum of three given integers. However, if
two values are equal sum will be zero. 
"""

# Program to find the sum of three integers
# If any two values are equal, the sum will be zero

a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
c = int(input("Enter third integer: "))

if a == b or b == c or a == c:
    total = 0
else:
    total = a + b + c

print("Result:", total)