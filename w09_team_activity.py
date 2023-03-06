print('Enter a list of numbers, type 0 when finished.')
print('')
number_list = []
number = -1
while number != 0:
    number = int(input('Enter a number: '))
    if number != 0:
        number_list.append(number)
total = 0
for number in number_list:
    total += number
print(total)
