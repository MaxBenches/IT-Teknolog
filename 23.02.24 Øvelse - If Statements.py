"""
# 1. assign 20 to the variable y and 40 to the variable z, but only if the variable x is over 100
x = int(input("Please enter an integer "))

if x >= 100:
    y = 20
    z = 40
    print(x, y, z)
else:
    print("That's a good number right there!")
"""

"""
# 2. assign 10 to the variable b and 50 to the variable c, but only if the variable a is equal to 100
a = int(input("Please enter an integer "))

if a == 100:
    b = 10
    c = 50
    print(a, b, c)
else:
    print("That's a good number right there!")
"""


# 3. if the variable a is less than 10, b is assigned 0, if not b is assigned 99
a = int(input("Please enter an integer "))

if a < 10:
    b = 0
    print(a, b)
else:
    b = 99
    print(a, b)