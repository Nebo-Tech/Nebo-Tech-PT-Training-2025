import math

def area_of_circle():
    r=float(input('Enter the radius of the circle:'))
    area= math.pi * r**2
    print("r=",r)
    print("Area=",area)

area_of_circle()