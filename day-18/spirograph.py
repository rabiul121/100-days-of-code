import random
import turtle as t

turtle = t.Turtle()
turtle.color("red")
t.colormode(255)
turtle.speed("fastest")
turtle.pensize(1)


def generate_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        turtle.color(generate_color())
        turtle.circle(100)
        turtle.setheading(turtle.heading() + size_of_gap)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
