# Get amount of grades to be averaged

LIST_START = 0

list_end = int(input("How many grades need to be averaged? "))

# Loop to check if there are more grades

for user_list in range(LIST_START, list_end):
    grade_grade = int(input("What is the grade? "))
    grade_total = grade_total + grade_grade