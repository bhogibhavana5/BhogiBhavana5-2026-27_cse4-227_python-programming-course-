
# Create a list with duplicate elements
numbers = [10, 20, 30, 20, 40, 10, 50, 30]

print("Original list:", numbers)

# Convert list into a set to remove duplicates
unique_set = set(numbers)

# Convert set back into a list
unique_list = list(unique_set)

# Display the result
print("List after removing duplicates:", unique_list)

