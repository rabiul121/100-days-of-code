import random
import turtle

colors = [(236, 232, 73), (219, 150, 100), (98, 248, 160), (141, 78, 40), (166, 6, 107), (33, 21, 172), (232, 53, 182), (226, 128, 203), (21, 202, 69), (22, 103, 174), (27, 135, 65), (129, 152, 230), (55, 225, 93),
          (166, 17, 4), (81, 87, 236), (190, 35, 148), (180, 181, 244), (239, 72, 40), (199, 156, 15), (233, 158, 216), (16, 27, 102), (59, 7, 252), (96, 10, 67), (87, 245, 249), (173, 240, 0), (11, 193, 199)]


t = turtle.Turtle()
t.speed(0)
t.penup()
t.hideturtle()
turtle.colormode(255)

dot_size = 30
dot_spacing = 50

for row in range(10):
    for col in range(10):
        x = col * dot_spacing - 225
        y = row * dot_spacing - 225

        t.goto(x, y)

        t.dot(dot_size, random.choice(colors))


turtle.done()
