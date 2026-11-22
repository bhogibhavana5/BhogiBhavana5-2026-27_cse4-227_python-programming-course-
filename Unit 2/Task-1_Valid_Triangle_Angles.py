# Read three angles
a = int(input("Enter the first angle: "))
b = int(input("Enter the second angle: "))
c = int(input("Enter the third angle: "))

# Check whether the triangle is valid
if a > 0 and b > 0 and c > 0 and a + b + c == 180:
    print("The triangle is valid")
else:
    print("The triangle is not valid")
