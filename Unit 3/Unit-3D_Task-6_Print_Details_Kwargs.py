def print_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

# Calling the function with keyword arguments
print_details(name="Krishna", age=26, city="Guntur")
