# import colorgram
#
# colors = colorgram.extract('paint.jpg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle
import random

t = turtle.Turtle()
s = turtle.Screen()
turtle.colormode(255)
t.speed(0)
t.penup()
t.hideturtle()
t.setheading(225)
t.forward(300)
t.setheading(0)
number_of_dots = 100

colors = [(236, 232, 73), (219, 150, 100), (98, 248, 160), (141, 78, 40), (166, 6, 107), (33, 21, 172), (232, 53, 182), (226, 128, 203), (21, 202, 69), (22, 103, 174), (27, 135, 65), (129, 152, 230), (55, 225, 93),
          (166, 17, 4), (81, 87, 236), (190, 35, 148), (180, 181, 244), (239, 72, 40), (199, 156, 15), (233, 158, 216), (16, 27, 102), (59, 7, 252), (96, 10, 67), (87, 245, 249), (173, 240, 0), (11, 193, 199)]

for dot_count in range(1, number_of_dots + 1):
    t.dot(20, random.choice(colors))
    t.forward(50)

    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)

turtle.done()
