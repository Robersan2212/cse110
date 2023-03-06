menu= [
    '1-drink',
    '2 - Entree',
    '3 - side',
    '4 - dessert'
]
selection = 0
selections = []
print("menu: ")
for item in menu:
    print(f' {item} ')

selection = int(input('What would you like to order? '))

print(f'You selected {selection}')
print()