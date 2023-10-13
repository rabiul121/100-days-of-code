import turtle
import random

# Set up the turtle screen
screen = turtle.Screen()

# Set up the turtle pen
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
turtle.colormode(255)
pen.hideturtle()

colors = [(236, 232, 73), (219, 150, 100), (98, 248, 160), (141, 78, 40), (166, 6, 107), (33, 21, 172), (232, 53, 182), (226, 128, 203), (21, 202, 69), (22, 103, 174), (27, 135, 65), (129, 152, 230), (55, 225, 93),
          (166, 17, 4), (81, 87, 236), (190, 35, 148), (180, 181, 244), (239, 72, 40), (199, 156, 15), (233, 158, 216), (16, 27, 102), (59, 7, 252), (96, 10, 67), (87, 245, 249), (173, 240, 0), (11, 193, 199)]

# Define the dot size and spacing
dot_size = 30
dot_spacing = 50

# Loop through rows and columns to draw dots
for row in range(10):
    for col in range(10):
        # Calculate the dot position
        x = (col * dot_spacing) - 225
        y = (row * dot_spacing) - 225

        # Move the pen to the dot position
        pen.goto(x, y)

        # Draw the dot
        pen.dot(dot_size, random.choice(colors))


# Keep the turtle screen open until closed manually
turtle.done()
