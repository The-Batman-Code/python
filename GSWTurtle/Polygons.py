from turtle import Turtle, Screen
import random
import turtle
batman = Turtle()
turtle.colormode(255)
batman.width(5)
for i in range(3, 11):
    batman.color(random.randint(0, 255), random.randint(
        0, 255), random.randint(0, 255))
    for a in range(0, i):
        batman.forward(100)
        batman.right(360/i)
screen = Screen()
screen.exitonclick()
