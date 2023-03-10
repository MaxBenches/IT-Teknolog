# Import randomisation library
import random   # Imports random library

# Assign a randomly generated number to the PC's choice of rock, paper or scissor
pc_choice = (random.randrange(1,4))
if pc_choice == 1:
    pc_choice = "Rock"
elif pc_choice == 2:
    pc_choice = "Paper"
elif pc_choice == 3:
    pc_choice = "Scissors"

# Get player choice
player_choice = input("Please enter your choice: Rock, Paper or Scissors\n")
"""
if pc_choice == "Rock" or "rock":
    pc_choice = 1
elif pc_choice == "Paper" or "paper":
    pc_choice = 2
elif pc_choice == "Scissors" or "Scissors":
    pc_choice = 3
"""

# Display PC choice
print(f'PC has chosen {pc_choice}')

# Select winner
if pc_choice == "Rock" and player_choice == "Scissors":
    print("Rock smahes Scissors. You lose!")
elif pc_choice == "Scissors" and player_choice == "Rock":
    print("Rock smahes Scissors. You win!")
elif pc_choice == "Scissors" and player_choice == "Paper":
    print("Scissors cut Paper. You lose!")
elif pc_choice == "Paper" and player_choice == "Scissors":
    print("Scissors cut Paper. You win!")
elif pc_choice == "Paper" and player_choice == "Rock":
    print("Paper wraps Rock. You lose!")
elif pc_choice == "Rock" and player_choice == "Paper":
    print("Paper wraps Rock. You win!")
else:
    print(f'PC and Player have both chosen {pc_choice}')
# A while loop might be necessary with the above code nested inside?