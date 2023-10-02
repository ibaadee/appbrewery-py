import turtle as t
import random

t.colormode(255)

tim = t.Turtle()
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

screen = t.Screen()
screen.exitonclick()