import turtle as t
import random as r

t.colormode(255)
color_list = [(228, 228, 227), (246, 236, 243), (243, 243, 246), (233, 166, 59), (46, 112, 157), (113, 150, 203), (212, 123, 164), (17, 128, 96), (171, 45, 87), (2, 177, 143)]

tim = t.Turtle()
tim.penup()
tim.hideturtle()

dots_per_row = 10
number_of_row = 10

def paint_row(dots_number):
    for _ in range(dots_number):
        tim.dot(20, r.choice(color_list))
        tim.forward(50)

def move_to_upper_row(dots_number):
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(50*dots_number)
    tim.setheading(0)

tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for _ in range (number_of_row):
    paint_row(dots_per_row)
    move_to_upper_row(dots_per_row)

screen = t.Screen()
screen.exitonclick()