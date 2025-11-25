"""
Write a Python program to count occurrences of a substring in a string.  """

string = input("Enter the main string: ")
substring = input("Enter the substring to count: ")

# Use count() method to count occurrences
count = string.count(substring)

# Display the result
print(f"The substring '{substring}' occurs {count} times in the given string.")


 
                                     