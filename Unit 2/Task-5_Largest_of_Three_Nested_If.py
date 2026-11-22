# Read three numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

# Find the largest number using nested if
if a >= b:
    if a >= c:
        largest = a
    else:
        largest = c
else:
    if b >= c:
        largest = b
    else:
        largest = c

# Display the result
print("The largest number is:", largest)
