def shopping_cart(**products):
    total = 0

    print("Shopping Cart:")
    for item, price in products.items():
        print(item, ": ₹", price)
        total += price

    print("Total Price: ₹", total)

# Calling the function
shopping_cart(apple=15, orange=12, mango=10)
