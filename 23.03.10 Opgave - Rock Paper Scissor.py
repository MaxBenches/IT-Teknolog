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

# Display PC choice
print(f'PC has chosen {pc_choice}')