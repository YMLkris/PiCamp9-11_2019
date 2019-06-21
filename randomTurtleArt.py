from turtle import *
import random

turtle = Turtle()
screen = Screen()
screen.bgcolor(0,0,0)
turtle.penup()
turtle.speed(100)
turtleColor = ["red", "green", "orange", "green", "lightgreen", "aqua", "blue", "lightblue", "pink", "yellow", "purple"]
turtleShape = ["turtle", "arrow", "square", "circle", "triangle"]

for i in range(200):
    random.shuffle(turtleColor)
    random.shuffle(turtleShape)
    turtle.color(turtleColor[0])
    turtle.shape(turtleShape[0])
    x = random.randint(-300,300)
    y = random.randint(-300,300)
    turtle.goto(x,y)
    turtle.left(random.randint(0,90))
    turtle.stamp()