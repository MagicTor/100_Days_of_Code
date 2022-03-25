###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import turtle
import random
'''
rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append((color.rgb[0],color.rgb[1],color.rgb[2]))

print(rgb_colors)
'''
turtle.colormode(255)
color_list = [(149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
# Dots should be 20 in size and spread by at least 30 paces
obj = turtle.Turtle()
obj.speed("fastest")
obj.penup()
obj.hideturtle()
for y in range(-150, 211, 40):
    obj.setposition(-250, y)
    for i in range(10):
        obj.dot(20, random.choice(color_list))
        obj.forward(40)


screen = turtle.Screen()
screen.exitonclick()
