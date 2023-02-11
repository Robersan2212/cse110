import math as M
childs_meal = float(input("What is the price of a child's meal? $"))
adults_meal = float(input("What is the price of an adult's meal? $"))
drinks = float(input("What is the price of the drinks? $"))
appetizers = float(input("What is the price od the appetizers? $"))
number_children = int(input("How many children are there? "))
number_adults = int(input("How many adults are there? "))
sales_tax_rate = float(input("What is the sales tax rate? "))
tip = int(input("How much would you like to leave for a tip? %"))
print('')
print('')
sub_totatl_children = number_children * childs_meal
sub_total_adult = number_adults * adults_meal
sub_total = sub_totatl_children + sub_total_adult + appetizers + ((number_children + number_adults) * drinks)
sales_tax_total = sub_total * sales_tax_rate /100
total_meal1 = sub_total + sales_tax_total 
tip_total = tip / 100 * sub_total
total_meal = total_meal1 + tip_total 
randon1 = number_children + number_adults * drinks
print(f'Subtotal: ${sub_total}')
print(f"Tip: {tip_total: ,.2f}")
print(f'Sales Tax: ${sales_tax_total}')
print(f'Total: ${total_meal: ,.2f}')
print('')
print('')
payment_amount = int(input('What is the payment amount? $'))
change = payment_amount - total_meal
print(f'Change: ${change: ,.2f}')
print('Have a wonderful day :)')
