def simple_interest(principal, time, rate=5):
    si = (principal * time * rate) / 100
    return si

# Calling the function with the default rate
si1 = simple_interest(10000, 2)
print("Simple Interest with default rate:", si1)

# Calling the function with an explicit rate
si2 = simple_interest(10000, 2, 8)
print("Simple Interest with explicit rate:", si2)
