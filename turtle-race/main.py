from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
colors = ['red', 'orange', 'yellow', 'blue', 'green', 'purple']
not_valid_bet = True
while not_valid_bet:
    user_bet = screen.textinput(title='Make your bet', prompt="Which turtle will win the race? Enter a color: ").lower()
    if user_bet in colors:
        not_valid_bet = False
print(user_bet)
y_positions = [-100, -60, -20, 20, 60, 100]
all_turtles = []


if user_bet:
    for turtle_index in range(0, 6):
        new_turtle = Turtle(shape='turtle')
        new_turtle.color(colors[turtle_index])
        new_turtle.penup()
        new_turtle.goto(x=-235, y=y_positions[turtle_index])
        all_turtles.append(new_turtle)
    is_race_on = True
    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print("You've won!")
                else:
                    print("You've lost!")
                print(f"The {winning_color} turtle is the winner!")
            rand_distance = random.randint(0,10)
            turtle.forward(rand_distance)

screen.exitonclick()
