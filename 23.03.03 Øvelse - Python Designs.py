import turtle

def main():
    turtle.setup(1440, 810, 50, 300)
    turtle.speed(5)
    turtle.hideturtle()
    #turtle.dot(10)
    #drawTriangle(200)
    #drawSquare(200)
    #drawPentagon(200)
    #drawHexagon(200)
    drawPenis(100)
    turtle.done()

def drawTriangle(size):
    # Centers the turtle in relation to the triangle
    xStart = size / -2
    yStart = size / -3
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(xStart, yStart)
    turtle.showturtle()
    turtle.pendown()
    for i in range(3):
        turtle.forward(size)
        turtle.left(120)

def drawSquare(size):
    # Centers the turtle in relation to the square
    xStart = size / -2
    yStart = size / 2
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(xStart, yStart)
    turtle.showturtle()
    turtle.pendown()
    # Draws the square
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)

def drawPentagon(size):
    # Centers the turtle in relation to the pentagon
    xStart = size / -2
    yStart = size / -1.618
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(xStart, yStart)
    turtle.showturtle()
    turtle.pendown()
    # Draws the pentagon
    for i in range(5):
        turtle.forward(size)
        turtle.left(72)

def drawHexagon(size):
    # Centers the turtle in relation to the hexagon
    xStart = size / -2
    yStart = size / -1.2
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(xStart, yStart)
    turtle.showturtle()
    turtle.pendown()
    # Draws the hexagon
    for i in range(6):
        turtle.forward(size)
        turtle.left(60)


def drawPenis(size):
    # Draws the first nut
    turtle.penup()
    turtle.goto(0 , -size*2)
    turtle.right(90)
    turtle.pendown()
    turtle.circle(size , 270)
    # Draws the second nut
    turtle.penup()
    turtle.goto(0 , -size*2)
    turtle.left(90)
    turtle.pendown()
    turtle.circle(-size , 270)
    # Draws the shaft
    turtle.left(90)
    turtle.forward(size * 3)
    turtle.penup()
    turtle.goto(size, -size)
    turtle.pendown()
    turtle.forward(size * 3)
    # Draws the head
    turtle.right(90)
    turtle.forward(size / 5)
    turtle.right(90)
    turtle.circle(-size * 1.2 , -90)
    turtle.right(90)
    turtle.forward(size/3)
    turtle.right(180)
    turtle.forward(size/3)
    turtle.right(90)
    turtle.circle(-size * 1.2 , -90)
    turtle.right(90)
    turtle.forward(size / 5)




main()