import turtle

t = turtle.Turtle()
s = turtle.Screen()


def move_forward():
    t.forward(10)


def move_backward():
    t.backward(10)


def turn_left():
    t.left(10)


def turn_right():
    t.right(10)


def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


s.listen()
s.onkey(key="d", fun=move_forward)
s.onkey(key="a", fun=move_backward)
s.onkey(key="w", fun=turn_left)
s.onkey(key="s", fun=turn_right)
s.onkey(key="c", fun=clear)

s.exitonclick()
