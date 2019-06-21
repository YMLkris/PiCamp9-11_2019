from turtle import *

turtle = Turtle()
screen = Screen()
# turtle shapes: “arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”
screen.bgcolor(1,0,0)
turtle.pendown()

for j in range(10):
    for i in range(2):
        turtle.forward(100)
        turtle.right(60)
        turtle.forward(100)
        turtle.right(120)
    turtle.right(36)

