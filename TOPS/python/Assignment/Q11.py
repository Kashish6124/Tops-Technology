"""
Write a Python program to test whether a passed letter is a vowel
or not. 

"""

# Program to check if a letter is a vowel

# take input from user
ch = input("Enter a letter: ")

# convert to lowercase so that it works for both upper & lower case
if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
    print(ch, "is a vowel.")
else:
    print(ch, "is not a vowel.")