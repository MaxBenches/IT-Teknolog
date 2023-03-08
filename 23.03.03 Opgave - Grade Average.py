# This program takes a user specified number of grades and calculates the average

LIST_START = 0                                                      # End of the loop
list_end = int(input("How many grades need to be averaged? "))      # Start of the loop

# Start accumulator
grade_total = 0

# Get the grades from user and accumulate them
for user_list in range(LIST_START, list_end):
    grade_number = int(input("Please enter a grade: "))
    grade_total = grade_total + grade_number

# Calculate average and display the average of grades
grade_avg = grade_total/list_end
print(f'The average grade is {grade_avg:.2f}.')