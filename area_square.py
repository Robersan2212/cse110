import math as m 
def area_square(sides):
    return sides * sides
def area_circle(radius): 
    return m.pi * radius * radius
def area_rectangle(length, width):
    length * width

shape = "square"

while shape in ["square", "circle", "rectangle"]:
    shape = input("What shape are we working on? ")
    if shape == "square":
       sides = int(input('What are the sides of the square? '))
       compute_square = area_square(sides)
       print(f'The area of the square is: {compute_square}')
    if shape == "circle":
        radius = float(input('What is the radius of the circle? '))
        compute_circle = area_circle(radius)
        print(f'The are of the circle is : {compute_circle}')
    if shape == "rectangle":
        length = float(input('What is the length of the rectangle? '))
        width = float(input('What is the width? '))
        compute_rectangle = area_rectangle(length, width)
        print(f'{compute_rectangle}')
    
    
    
