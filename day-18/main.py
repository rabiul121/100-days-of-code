from turtle import Turtle, Screen

turtle = Turtle()
for n in range(15):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()

screen = Screen()
screen.exitonclick()
