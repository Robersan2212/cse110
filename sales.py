import math as M
sales = float(input('How much was the sale for: '))
sales_rounded = round(sales, 2)
print(f'The sales was for $ {sales: ,.2f} or {sales_rounded}')