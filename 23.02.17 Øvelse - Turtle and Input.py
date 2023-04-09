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
    turtle.done()


# This function prompts the user to input a diameter
# It then halves this, so the turtle can use it as a radius
def getRadius():
    userDiameter = int(input("What is the diameter of the circle you want drawn? "))
    userRadius = userDiameter / 2
    return userRadius

# This function prompts the user to input an X value for the turtle's starting point
def getXCoord():
    userXCoord = int(input("Where would you like the circle to start on the X axis? "))
    return userXCoord

# This function prompts the user to input an Y value for the turtle's starting point
def getYCoord():
    userYCoord = int(input("Where would you like the circle to start on the y axis? "))
    return userYCoord

main()
