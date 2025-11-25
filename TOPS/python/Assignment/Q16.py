"""Write a Python program to count the number of characters
(character frequency) in a string  """

text = input("Enter a string: ")

# remove duplicates by converting to set
for ch in set(text):
    count = 0
    for c in text:
        if c == ch:
            count += 1
    print(ch, ":", count)
