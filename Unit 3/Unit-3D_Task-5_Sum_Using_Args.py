def find_sum(*args):
    total = 0
    for num in args:
        total += num
    return total

# Calling the function with different numbers of arguments
print("Sum of 3 numbers:", find_sum(10, 20, 30))
print("Sum of 5 numbers:", find_sum(1, 2, 3, 4, 5))
print("Sum of values:", find_sum(5, 10, 15, 20))
