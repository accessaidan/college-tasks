import turtle

blue = "#0000ff"
pink = "#ff00ff"
green = "#00ff00"

def drawsquare(size, colour):
    turtle.pendown()
    turtle.color(colour)
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)
    
    turtle.penup()

turtle.speed(5)
turtle.setheading(0)
drawsquare(100,blue)
turtle.forward(90)
turtle.right(90)
turtle.forward(10)
drawsquare(80,pink)
