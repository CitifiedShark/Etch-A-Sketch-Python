from turtle import Turtle, Screen
import random

screen = Screen()
turtle = Turtle()

# set speed
turtle.speed('fastest')

# movement functions
def move_forward():
    turtle.forward(25)

def turn_left():
    new_heading = turtle.heading() + 10
    turtle.setheading(new_heading)

def move_back():
    turtle.backward(25)

def turn_right():
    new_heading = turtle.heading() - 10
    turtle.setheading(new_heading)

def clear():
    screen.resetscreen()
    turtle.setx(0)
    turtle.sety(0)


# gather keyboard input
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='s', fun=move_back)
screen.onkey(key='d', fun=turn_right)

screen.onkey(key='c', fun=clear)

# close window
screen.exitonclick()
