from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.tracer(0)

paddle_one = Paddle(-350, 0)
paddle_two = Paddle(350, 0)

ball = Ball()

screen.listen()
screen.onkey(paddle_one.move_up, 'w')
screen.onkey(paddle_one.move_down, 's')
screen.onkey(paddle_two.move_up, 'Up')
screen.onkey(paddle_two.move_down, 'Down')
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')


game_is_on = True
while game_is_on:
    time.sleep(.1)
    screen.update()
    ball.move()



screen.exitonclick()