# Program to demonstrate use of pass statement

print("1. pass in for loop:")
for i in range(1, 6):
    if i == 3:
        pass  # do nothing when i is 3, just skip
    else:
        print(f"i = {i}")
print("pass executed, loop continued\n")

print("2. pass in while loop:")
count = 0
while count < 5:
    count += 1
    if count == 3:
        pass  # placeholder, does nothing
    else:
        print(f"count = {count}")
print("pass executed, loop continued")
