# import colorgram
# colors = colorgram.extract('hirst_painting.jpg', 50)
# color_list = []
# for color in colors:
#     r, g, b = color.rgb
#     color_list.append((r, g, b))
#
# print(color_list)

from turtle import Turtle, Screen, colormode
import random

colormode(255)

jesus = Turtle()

color_list = [(134, 164, 200), (221, 153, 105), (30, 42, 61), (201, 136, 147), (156, 64, 53), (235, 213, 90), (48, 101, 143), (137, 181, 162), (149, 63, 72), (166, 27, 34), (51, 46, 43), (158, 31, 26), (53, 41, 44), (60, 114, 98), (231, 163, 169), (237, 166, 157), (213, 82, 69), (33, 59, 53), (16, 95, 70), (198, 94, 104), (170, 189, 221), (34, 60, 105), (108, 125, 161), (20, 81, 102), (173, 201, 191), (35, 152, 207), (162, 203, 217), (93, 147, 136), (65, 66, 57), (203, 146, 48), (250, 203, 4)]
print(jesus.pos())

y = -300
for blah in range(0, 10):
    if blah >= 1:
        y += 50
    jesus.penup()
    jesus.sety(y)
    jesus.setx(-200)
    for num in range(0, 10):
        jesus.pendown()
        jesus.dot(20, random.choice(color_list))
        jesus.penup()
        jesus.forward(50)

jesus.ht()
screen = Screen()
screen.exitonclick()