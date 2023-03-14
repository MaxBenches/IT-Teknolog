# Import randomisation library
import random   # Imports random library

# Placeholders to initialise "draw" loop
pc_choice = 0
player_choice = 0

# Loop to start over if pc and player chooses the same
while pc_choice == player_choice.lower():
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
    # Display draw message and start over
    if pc_choice == player_choice:
        print(f"PC and Player have both chosen {pc_choice}. It's a draw!\n"
              f"Please play again to determine a winner.\n")

# Display PC choice
print(f'PC has chosen {pc_choice}')

# Select and display winner
if pc_choice == "Rock" and player_choice == "Scissors":
    print("Rock smashes Scissors. You lose!")
elif pc_choice == "Scissors" and player_choice == "Rock":
    print("Rock smashes Scissors. You win!")
elif pc_choice == "Scissors" and player_choice == "Paper":
    print("Scissors cut Paper. You lose!")
elif pc_choice == "Paper" and player_choice == "Scissors":
    print("Scissors cut Paper. You win!")
elif pc_choice == "Paper" and player_choice == "Rock":
    print("Paper wraps Rock. You lose!")
elif pc_choice == "Rock" and player_choice == "Paper":
    print("Paper wraps Rock. You win!")
