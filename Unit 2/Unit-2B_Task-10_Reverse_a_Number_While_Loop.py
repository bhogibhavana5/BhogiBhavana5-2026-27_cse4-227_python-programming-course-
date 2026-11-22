# Read a number
num = int(input("Enter a number: "))

# Initialize reverse
reverse = 0

# Reverse the number
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

# Display the result
print("Reversed number =", reverse)
