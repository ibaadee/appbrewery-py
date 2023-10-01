from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("green")

def draw_shape(num):
    angle = 360/num
    for _ in range(num):
            tim.forward(100)
            tim.right(angle)

for side_number in range (3, 11):
    tim.color(random.random(), random.random(), random.random())
    draw_shape(side_number)

screen = Screen()
screen.exitonclick()