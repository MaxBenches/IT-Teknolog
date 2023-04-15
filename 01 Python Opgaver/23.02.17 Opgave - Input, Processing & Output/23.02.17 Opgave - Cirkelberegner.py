# Input hvor stor radius er
radius = float(input("Hvad er radius på din cirkel i centimeter? "))

# Udregn areal efter given radius
PI = 3.1415926535 

# Udregn areal og print
area = PI*radius**2
print("Arealet af cirklen er:",area,"centimeter.")

# Udregn omkreds og print
circumference = 2*PI*radius
print("Omkredsen af cirklen er:",circumference,"centimeter.")