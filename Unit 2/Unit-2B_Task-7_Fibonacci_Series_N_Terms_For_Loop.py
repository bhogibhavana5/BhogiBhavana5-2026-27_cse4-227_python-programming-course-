# Read the number of terms
n = int(input("Enter the number of terms: "))

# Initialize first two terms
a = 0
b = 1

# Print Fibonacci series
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
