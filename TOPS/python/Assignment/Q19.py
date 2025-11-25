# Write a Python program to count the occurrences of each word in a given sentence

string = input("Enter a sentence: ")

string = string.lower()       # Step 1: make everything lowercase
words = string.split()        # Step 2: split sentence into words

word_count = {}               # Step 3: create an empty dictionary

for word in words:            # Step 4: go through each word
    if word in word_count:    
        word_count[word] += 1  # if already exists, add +1
    else:
        word_count[word] = 1   # if not, set count = 1

print("Word occurrences:")    # Step 5: print result
for word, count in word_count.items():
    print(f"{word}: {count}")