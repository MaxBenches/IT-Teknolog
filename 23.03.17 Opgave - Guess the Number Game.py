# Make a program that generates a random number between 1 and 100
# Ask the player to guess the number
# Tell the player if the number is higher or lower
# Continue until the user guesses the right number
# Print out the total number of guesses, this is the score and must be as low as possible.
# You must use functions, ex. getRandomNumber(), checkNumber()
# Create a flow chart of your program (one flow for each function)
# Creat IPO charts for each function.

import random

def guessTheNumber():
    pcNum = getRandNum()
    #print(pcNum)                   # Shows the number to be guessed. Used for testing
    userGuess = 999                 # Initialise userGuess variable
    totalGuess = 0                  # Initialise accumulator
    while pcNum != userGuess:       # Loop as long as userGuess is different from pcNum
        userGuess = getUserGuess()
        checkGuess(pcNum,userGuess)
        totalGuess += 1
        #print(totalGuess           # Shows how many guesses for every iteration. Used for testing
    print(f"\nYou guessed correctly! The number was {pcNum}.")
    if totalGuess <= 5:
        print(f"Your total number of guesses: {totalGuess}. Well done!")
    else:
        print(f"Your total number of guesses: {totalGuess}. Better luck next time!")


# This function generates a random number
def getRandNum():
    randNum = random.randint(0,100)
    return randNum

# This function gets the user's guess
def getUserGuess():
    userGuess = int(input("Please enter your guess: "))
    return userGuess

# This function checks if the user's guess is higher or lower than the random number
def checkGuess(pcNum,userGuess):
    if userGuess < pcNum:
        print("Your guess was too low. Please try again.")
    elif userGuess > pcNum:
        print("Your guess was too high. Please try again.")

guessTheNumber()