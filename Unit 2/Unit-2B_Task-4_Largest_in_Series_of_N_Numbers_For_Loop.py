# Read the number of values
n = int(input("Enter how many numbers: "))

# Read the first number
largest = float(input("Enter number: "))

# Find the largest number
for i in range(1, n):
    num = float(input("Enter number: "))

    if num > largest:
        largest = num

# Display the result
print("Largest number =", largest)
