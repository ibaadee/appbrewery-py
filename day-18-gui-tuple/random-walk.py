from turtle import Turtle, Screen
import random

colors = ["royal blue", "spring green", "sandy brown", "medium orchid", "light slate gray"]
directions = [0, 90, 180, 270]

tim = Turtle()
tim.shape("turtle")
tim.speed(0)
tim.pensize(15)

for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()