# Read the number of values
n = int(input("Enter how many numbers: "))

total = 0

# Read and calculate the sum
for i in range(1, n + 1):
    num = float(input("Enter number: "))
    total = total + num

# Calculate average
average = total / n

# Display results
print("Sum =", total)
print("Average =", average)
