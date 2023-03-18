"""
# This program takes two resistor values, calculates the
# total resistance and prints it

def main():
    res1 = float(input("Please enter the value of the 1st resistor in ohms: "))
    res2 = float(input("Please enter the value of the 2nd resistor in ohms: "))
    calc_total_res(res1,res2)

# Function to calculate and display the total resistance
def calc_total_res(res1, res2):
    total_res = 1/ ((1/res1)+(1/res2))
    print(f"The total resistance is: {total_res} ohms")

# Calling the main function
main()
"""


# This program generates a random number
# between 0 and 100, and displays it
import random

def main():
    random_number()


def random_number():
    number = random.randint(1,100)
    print(f'Your randomly generated number is {number}.')

main()