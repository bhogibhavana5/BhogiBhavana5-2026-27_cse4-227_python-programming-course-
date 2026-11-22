# Read a three-digit number
num = int(input("Enter a three-digit number: "))

# Store the original number
original = num

# Initialize sum
total = 0

# Calculate the sum of cubes of digits
while num > 0:
    digit = num % 10
    total = total + digit ** 3
    num = num // 10

# Check Armstrong number
if total == original:
    print("The number is an Armstrong number")
else:
    print("The number is not an Armstrong number")
