# Read two numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Swap without using a third variable
a = a + b
b = a - b
a = a - b

# Display the swapped numbers
print("After swapping:")
print("First number =", a)
print("Second number =", b)
