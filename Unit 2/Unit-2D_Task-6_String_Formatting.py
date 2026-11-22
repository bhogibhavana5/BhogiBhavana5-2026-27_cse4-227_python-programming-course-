name = "Bhavana"
age = 18
marks = 95.5

# Using format()
print("Using format():")
print("My name is {} and my age is {}".format(name, age))

# Using f-strings
print("\nUsing f-strings:")
print(f"My name is {name} and my age is {age}")

# Using % operator
print("\nUsing % operator:")
print("My name is %s and my age is %d" % (name, age))

# Formatting floating-point numbers
print("\nMarks using format(): {:.2f}".format(marks))
print(f"Marks using f-string: {marks:.2f}")
print("Marks using % operator: %.2f" % marks)
