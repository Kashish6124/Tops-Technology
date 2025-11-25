"""Write python program that swap two number with temp variable
and without temp variable"""

# Swapping two numbers using a temporary variable
print("Swap using temp variable:")
a = 10
b = 20
print("Before swapping: a =", a, "b =", b)

temp = a
a = b
b = temp

print("After swapping: a =", a, "b =", b)

print("\n-------------------------\n")

# Swapping two numbers without using a temporary variable
print("Swap without temp variable:")
x = 5
y = 15
print("Before swapping: x =", x, "y =", y)

# Method 1: Using arithmetic operations
x = x + y
y = x - y
x = x - y

print("After swapping (arithmetic): x =", x, "y =", y)