# Read a number
num = int(input("Enter a number between 1 and 100: "))

# Check whether the number is prime
if num <= 1:
    print("The number is not prime")
else:
    for i in range(2, num):
        if num % i == 0:
            print("The number is not prime")
            break
    else:
        print("The number is prime")
