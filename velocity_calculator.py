import math as M
m = int(input('Mass in Kg: '))
g = float(input('Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): '))
t = int(input('Time in seconds: '))
p = float(input('Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): '))
A = float(input('Cross sectional area (in m^2): '))
C = float(input('Drag constant (0.5 for sphere, 1.1 for cylinder): '))
c = (1/2) * p * A * C
velocity_at_t = M.sqrt (m * g / c ) * (1 - M.exp((-M.sqrt(m * g * c) / m) * t))
print('')
print('')
print (f'The inner value of c is: {c: ,.3f} ')
print(f'The after 10.0 seconds is: {velocity_at_t: ,.3f} m/s ')
