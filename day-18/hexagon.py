import random
from turtle import Turtle, Screen

turtle = Turtle()
colors = ["lawn green", "dark orange", "medium slate blue", "gold", "deep sky blue", "black", "red", "dark slate blue",
          "indigo", "hot pink", "dark green", "maroon"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        turtle.forward(100)
        turtle.right(angle)


for shape_side_n in range(3, 11):
    turtle.color(random.choice(colors))
    draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()
