from turtle import Turtle, Screen
batman = Turtle()
screen = Screen()


def move_forward():
    batman.forward(10)


def move_backward():
    batman.backward(10)


def move_left():
    batman.left(5)


def move_right():
    batman.right(5)


def clear():
    batman.clear()
    batman.penup()
    batman.home()
    batman.pendown()


screen.onkey(move_forward, 'w')
screen.onkey(move_backward, 's')
screen.onkey(move_left, 'a')
screen.onkey(move_right, 'd')
screen.onkey(clear, 'c')


screen.listen()
screen.exitonclick()
