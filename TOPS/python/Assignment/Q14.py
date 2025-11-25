"""
Write a python program to sum of the first n positive integers
"""

# Program to find sum of first n positive integers

n = int(input("Enter a positive integer n: "))

# Formula method: n(n+1)/2
total = n * (n + 1) // 2   # use // for integer division

print("Sum of first", n, "positive integers is:", total)