# Read a number
num = int(input("Enter a number: "))

# Store the original number
original = num

# Initialize reverse
reverse = 0

# Reverse the number using while loop
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

# Check palindrome
if original == reverse:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")
