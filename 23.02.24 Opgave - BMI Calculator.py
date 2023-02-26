# Get height and weight
height = float(input("What is your height in meters? "))
weight = float(input("What is your weight in kilograms? "))
# Calculate BMI
bmi = weight/(height**2)
# Print BMI value and the associated category
if bmi >= 30:
    print(f'Your BMI is: {bmi:.2f}. That means you are obese.')
elif bmi >= 25:
    print(f'Your BMI is: {bmi:.2f}. That means you are overweight.')
elif bmi >= 18.6:
    print(f'Your BMI is: {bmi:.2f}. That means you are healthy.')
else:
    print(f'Your BMI is: {bmi:.2f}. That means you are thin.')