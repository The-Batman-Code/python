from turtle import Turtle, Screen
import random
import turtle
batman = Turtle()
turtle.colormode(255)
batman.speed(30)
for i in range(0, 73):
    batman.color(random.randint(0, 255), random.randint(
        0, 255), random.randint(0, 255))
    batman.circle(100)
    batman.left(5)
    batman.circle(100)

screen = Screen()
screen.exitonclick()
