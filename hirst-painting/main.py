import colorgram
import random
from turtle import Turtle, Screen

t = Turtle()
screen = Screen()
screen.colormode(255)
t.shape('turtle')
t.penup()
t.speed('fastest')
t.setheading(225)
t.forward(350)
t.setheading(0)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

color_list = [(226, 231, 235), (54, 108, 149), (225, 201, 108), (134, 85, 58),
 (229, 235, 234), (224, 141, 62), (197, 144, 171), (143, 180, 206),
 (137, 82, 106), (210, 90, 68)]


def row_of_dots():
    for _ in range(10):
        t.dot(20, random.choice(color_list))
        t.forward(50)


def set_for_new_row():
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(500)
    t.left(180)


for _ in range(10):
    row_of_dots()
    set_for_new_row()

screen.exitonclick()