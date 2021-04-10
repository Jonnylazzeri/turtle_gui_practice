from turtle import Turtle, Screen, colormode
import random

timmy = Turtle()
# timmy.shape('turtle')
timmy.color('IndianRed3')


def random_color():

    return random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)
# for _ in range(10):
#     timmy.forward(10)
#     timmy.pu()
#     timmy.forward(10)
#     timmy.pd()
#
colormode(255)
#
# for num in range(3, 11):
#     timmy.pencolor(random_color())
#     for n in range(num):
#         timmy.right(360 / num)
#         timmy.forward(100)
# timmy.pensize(10)
timmy.speed(0)
# for _ in range(200):
#     timmy.pencolor(random_color())
#     rand_num = random.randint(1, 4)
#     if rand_num == 1:
#         timmy.forward(20)
#     elif rand_num == 2:
#         timmy.left(90)
#         timmy.forward(20)
#     elif rand_num == 3:
#         timmy.right(90)
#         timmy.forward(20)
#     elif rand_num == 4:
#         timmy.right(180)
#         timmy.forward(20)
#

for _ in range(72):
    timmy.color(random_color())
    timmy.circle(100)
    timmy.left(5)

screen = Screen()
screen.exitonclick()

