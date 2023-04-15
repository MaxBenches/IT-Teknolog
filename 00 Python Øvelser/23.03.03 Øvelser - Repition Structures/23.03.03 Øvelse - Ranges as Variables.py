# Ask the user for a start value
list_start = int(input("Which number would you like your list to start from? "))

# Ask the user for an end value
list_end = int(input("Which number would you like your list to end at? "))
if list_end > list_start:
    #list_end = list_end + 1
    list_end += 1               # Augmented Assignment Operators - Samme som kodelinjen over

if list_end < list_start:
    #list_end = list_end - 1
    list_end -= 1               # Augmented Assignment Operator - Samme som kodelinjen over

# Ask the user for a step value
list_steps = int(input("In what steps should the list ascend or descend? "))

# Print out the number from ‘start’ to ‘end’ in ‘steps’ using a for loop with range
for user_list in range(list_start,list_end,list_steps):
    print(user_list)