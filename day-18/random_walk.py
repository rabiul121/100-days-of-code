import random
import turtle as t

turtle = t.Turtle()
t.colormode(255)


def generate_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


directions = [0, 90, 180, 270]
turtle.pensize(10)
turtle.speed("fast")

for _ in range(200):
    turtle.color(generate_color())
    turtle.forward(30)
    turtle.setheading(random.choice(directions))

screen = t.Screen()
screen.exitonclick()
