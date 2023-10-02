import turtle as t
import random

t.colormode(255)

tim = t.Turtle()
tim.speed(0)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_circle():
    tim.circle(100)

def tilt_angle(size_of_gap):
    tim.right(size_of_gap)

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        draw_circle()
        tilt_angle(size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()