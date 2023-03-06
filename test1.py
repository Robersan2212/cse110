# Define the product list
products = {
    "apple": 0.5,
    "banana": 0.25,
    "orange": 0.75,
    "grape": 1.5
}

# Define the shopping cart dictionary
cart = {}

# Define the function to add items to the cart
def add_item(item, quantity):
    if item in products:
        if item in cart:
            cart[item] += quantity
        else:
            cart[item] = quantity
    else:
        print("Sorry, we don't sell that product.")

# Define the function to remove items from the cart
def remove_item(item, quantity):
    if item in cart:
        if cart[item] > quantity:
            cart[item] -= quantity
        else:
            del cart[item]
    else:
        print("Item not in cart.")

# Define the function to display the cart contents
def display_cart():
    print("Shopping Cart:")
    if cart:
        for item in cart:
            print(f"{item}: {cart[item]} x {products[item]} = {cart[item] * products[item]}")
    else:
        print("Your cart is empty.")

# Define the main program loop
while True:
    print("Enter 'add' to add an item, 'remove' to remove an item, 'display' to display the cart contents, or 'quit' to exit.")
    choice = input("> ")
    if choice == "add":
        item = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        add_item(item, quantity)
    elif choice == "remove":
        item = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        remove_item(item, quantity)
    elif choice == "display":
        display_cart()
    elif choice == "quit":
        break
    else:
        print("Invalid choice.")
