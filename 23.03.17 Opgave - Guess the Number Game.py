# Make a program that generates a random number between 1 and 100
# Ask the player to guess the number
# Tell the player if the number is higher or lower
# Continue until the user guesses the right number
# Print out the total number of guesses, this is the score and must be as low as possible.
# You must use functions, ex. getRandomNumber(), checkNumber()
# Create a flow chart of your program (one flow for each function)
# Creat IPO charts for each function.

import random

def main():
    pcNum = getRandNum()
    print(pcNum)
    userGuess = 999
    while pcNum != userGuess:
        userGuess = getUserGuess()
        checkGuess(pcNum,userGuess)

# This function generates a random number
def getRandNum():
    randNum = random.randint(0,5)
    return randNum

# This function gets the user's guess
def getUserGuess():
    userGuess = int(input("Please enter your guess: "))
    return userGuess

# This function checks if the user's guess is higher or lower
def checkGuess(pcNum,userGuess):
    if userGuess < pcNum:
        print("Your guess was lower. Please try again.")
    elif userGuess > pcNum:
        print("Your guess was higher. Please try again.")

main()