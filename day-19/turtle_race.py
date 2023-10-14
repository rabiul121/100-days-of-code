import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)
turtle_color = ['red', 'green', 'blue violet', 'black', 'orange', 'blue']
turtle_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []
for i in range(0, 6):
    turtle = Turtle()
    turtle.penup()
    turtle.shape("turtle")
    turtle.goto(x=-230, y=turtle_position[i])
    turtle.color(turtle_color[i])
    all_turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 225:
            is_race_on = False
            winning_color = turtle.fillcolor()
            if winning_color == user_bet:
                print(f"You've won! {winning_color} turtle is the winner!")
            else:
                print(f"You have lost! {winning_color} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
