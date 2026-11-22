# Read a number
num = int(input("Enter a number: "))

# Initialize sum
total = 0

# Calculate sum of digits
while num > 0:
    digit = num % 10
    total = total + digit
    num = num // 10

# Display the result
print("Sum of digits =", total)
