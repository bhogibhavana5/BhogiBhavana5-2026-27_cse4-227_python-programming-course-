# Read a number
num = int(input("Enter a number: "))

# Initialize count
count = 0

# Count the digits
while num > 0:
    num = num // 10
    count = count + 1

# Display the result
print("Number of digits =", count)
