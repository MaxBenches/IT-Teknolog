# Write a program that draws a circle by obtaining information from the user:
# Inputs a diameter from the user
# Inputs an x position from the user
# Input a y position from the user
# Draws a circle with the diameter at position x,y
# Remember turtle.done()

import turtle

def main():
    turtle.setup(960,590,500,250)
    turtle.penup()
    turtle.goto(getXCoord(),getYCoord())
    turtle.pendown()
    turtle.circle(getRadius())
    print("Check the Turtle Graphics window to see your circle.")
    turtle.done()


# This function prompts the user to input a diameter
# It then halves this, so the turtle can use it as a radius
# Also validates the input
def getRadius():
    userDiameter = int(input("What is the diameter of the circle you want drawn?\n"
                             "Please input a positive integer between 1 and 200\n"))
    while userDiameter <= 0 or userDiameter > 100:
        print("The diameter cannot be a negative integer or above 100.\n"
              "Please enter a positive integer between 1 and 100.")
        userDiameter = int(input("What is the diameter of the circle you want drawn?\n"))
    userRadius = userDiameter / 2
    return userRadius

# This function prompts the user to input an X value for the turtle's starting point
# Also validates the input
def getXCoord():
    userXCoord = int(input("Where would you like the circle to start on the X axis?\n"
                           "Please input a value between -100 and 100.\n"))
    while userXCoord < -100 or userXCoord > 100:
        print("The entered value is not in the specified range.\n"
              "Please enter an integer between -100 and 100.")
        userXCoord = int(input("Where would you like the circle to start on the X axis?\n"))
    return userXCoord

# This function prompts the user to input a Y value for the turtle's starting point
# Also validates the input
def getYCoord():
    userYCoord = int(input("Where would you like the circle to start on the Y axis?\n"
                           "Please input a value between -100 and 100.\n"))
    while userYCoord < -100 or userYCoord > 100:
        print("The entered value is not in the specified range.\n"
              "Please enter an integer between -100 and 100.")
        userYCoord = int(input("Where would you like the circle to start on the Y axis?\n"))
    return userYCoord

main()
