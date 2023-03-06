again = 5
print('Welcome to the Shopping Cart Program: ')
print()

shopping_cart = [
'1. Add Item',
'2. View Cart',
'3. Remove Item',
'4. Compute Total',
'5. Quit'
]

selection = 0
selections =[]
while selection != 5:
    for options in shopping_cart:
        print(options)

    selection = int(input('Please enter an action: '))
    print(f'You have selected: {selection}')
    if selection == 1:
        selections.append(input('What item would you like to add? '))
    if selection == 2:
        print(f'You have added {selections} to your cart')
print('Thank you. Goodbye.')

