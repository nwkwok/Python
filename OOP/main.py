from turtle import Turtle, Screen
import random

screen = Screen()

tom = Turtle()
tom.speed('fastest')
tom.shape('turtle')
screen.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tom.color(random_color())
        tom.circle(100)
        tom.setheading(tom.heading() + size_of_gap)

draw_spirograph(2)


# color = ['CornflowerBlue', 'DarkOrchid', 'IndianRed', 'DeepSkyBlue', 'LightSeaGreen', 'Wheat']
# movement = ['forward', 'backward']
# direction = [0, 90, 180, 270]


# def draw_shape(number_of_sides):
#     angle = 360/number_of_sides
#     for _ in range(number_of_sides):
#         tom.forward(50)
#         tom.left(angle)

# for i in range(3, 20):
#     tom.color(random.choice(color))
#     draw_shape(i)
#     i += 1

# for _ in range(100):
#     tom.color(random.choice(color))
#     tom.forward(30)
#     tom.left(random.choice(direction))
#






screen.exitonclick()