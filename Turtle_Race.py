from turtle import Turtle, Screen
import random
screen = Screen()
turtle = Turtle()
turtle.hideturtle()
race_on = False
screen.setup(width=700, height=400)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions = [-70, -40, -10, 20, 50, 80]
turtles = []
user_guess = screen.textinput(
    title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')
while user_guess != 'red' and user_guess != 'orange' and user_guess != 'yellow' and user_guess != 'green' and user_guess != 'blue' and user_guess != 'purple':
    user_guess = screen.textinput(
        title='Enter the correct choice', prompt='Which turtle will win the race? Enter a color: ')
for i in range(0, 6):
    batman = Turtle(shape='turtle')
    batman.color(colors[i])
    batman.penup()
    batman.goto(x=-330, y=y_positions[i])
    turtles.append(batman)
race_on = True
while race_on:
    for i in turtles:
        if i.xcor() > 330:
            race_on = False
            win_col = i.pencolor()
            if win_col == user_guess:
                turtle.write(
                    f'You have won. The {win_col} turtle is the winner!!!', font='arial', align='center')
            else:
                turtle.write(
                    f'You have lost. The {win_col} turtle is the winner!!!', font='arial', align='center')
        i.forward(random.randint(0, 10))
screen.exitonclick()
