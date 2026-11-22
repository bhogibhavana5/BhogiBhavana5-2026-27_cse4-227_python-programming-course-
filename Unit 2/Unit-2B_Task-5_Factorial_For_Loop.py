# Read a number
n = int(input("Enter a number: "))

# Initialize factorial
fact = 1

# Calculate factorial using for loop
for i in range(1, n + 1):
    fact = fact * i

# Display the result
print("Factorial =", fact)
