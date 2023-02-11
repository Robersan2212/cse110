import math
mass = int(input('Mass (in kg): '))
gravity = float(input('Gravity (in m/s^2, 9.8 for earth, 24 for jupiter: '))
time = int(input('Time in seconds: '))
destiny_fluid = float(input('destiny of the fluid (in kg/m^3, 1.3 for air, 1000 for water): '))
cross_sectional_area = float(input('Cross sectional area (in m^2): '))
drag_constant = float(input('Drag constant (0.5 for sphere, 1.1 for cylinder): '))

the_inner_value_c = parce.int(destiny_fluid * drag_constant / gravity   (cross_sectional_area))