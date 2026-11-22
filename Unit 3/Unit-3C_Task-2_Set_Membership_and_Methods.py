
# Create a set
numbers = {10, 20, 30, 40, 50}

print("Original set:", numbers)

# Membership testing
print("Is 20 present?", 20 in numbers)
print("Is 60 present?", 60 in numbers)

# Add an element
numbers.add(60)
print("After adding 60:", numbers)

# Remove an element
numbers.remove(30)
print("After removing 30:", numbers)

# Discard an element
numbers.discard(10)
print("After discarding 10:", numbers)

# Discard a non-existing element
numbers.discard(100)
print("After discarding 100:", numbers)

