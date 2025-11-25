""" Write a Python program that will return true if the two given
integer values are equal or their sum or difference is 5. """

# Program to check if two integers are equal
# or their sum or difference is 5

a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))

if a == b or (a + b == 5) or (abs(a - b) == 5):
    print("True")
else:
    print("False")
