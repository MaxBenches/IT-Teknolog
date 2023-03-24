# Write a program that generates 100 random numbers and
# keep a count of how many of those random numbers are
# even and how many of them are odd.

import random

def main():
    for i in range(1):
        number = randNumber()
        print(number)
        evenOrOdd(number)



# Generate a random number
def randNumber():
    randNum = random.randint(0,5)
    return randNum

# Check of number is even or odd
def evenOrOdd(number):
    if number % 2 == 0:
        number = "Even"
    else:
        number = "Odd"
    return number

def countEvenOrOdd():


main()