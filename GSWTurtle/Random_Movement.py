from turtle import Turtle, Screen
import random
import turtle
batman = Turtle()
turtle.colormode(255)
batman.width(7)
batman.hideturtle()
batman.speed(5)
choices = [0, 90, 180, 270]
for i in range(50):
    batman.color(random.randint(0, 255), random.randint(
        0, 255), random.randint(0, 255))
    batman.forward(30)
    batman.right(choices[random.randint(0, 3)])
screen = Screen()
screen.exitonclick()
