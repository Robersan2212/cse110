
print()
print('Welcome to the Shopping Cart Program: ')
print()

shopping_cart = [
'1. Add Item',
'2. View Cart',
'3. Remove Item',
'4. Compute Total',
'5. Print Receipt',
'6. Quit'
]
i = 0
total = 0
selection = 0
price = 0
selections =[]
prices = []
while selection != 6:
    for options in shopping_cart:
        print(options)

    selection = int(input('Please enter an action: '))
    print(f'You have selected: {selection}')
    if selection == 1:
        selections.append(input('What item would you like to add? ').capitalize())
        price = float(input('What is the price of the item? $'))
        prices.append(price)
    print()
    if selection == 2:
        n = 0
        for i in range(len(selections)):
            n += 1
            final_price = prices[i]
            print(f'{n}. {selections[i]} - ${final_price:.2f}') 
    print()
    if selection == 3:
        index = int(input('What number of item in the list would you like to remove? '))
        selections.pop(index-1)
        prices.pop(index-1)
        print(f'You have removed "{index}" from your cart.')
    print()
    if selection == 4:
        total = 0
        for price in prices:
            total += price
        print(f'The total of the cart is: ${total:.2f}')
    print('')
    if selection == 5:
        print('---------------------------------------')
        n = 0
        total = 0
        for i in range(len(selections)):
            n += 1
            print(f'{n}. {selections[i]} - ${prices[i]:.2f}')
        for price in prices:
            total += price
        print(f'The total of the cart is: ${total:.2f}')
        print('---------------------------------------')
    print('')
            
print('Thank you. Have a good rest of your day!')
print('')
