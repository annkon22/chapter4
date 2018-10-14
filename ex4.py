#Invent an algorithm for drawing a fractal mountain

import turtle
import random as rnd


def draw_mount(points, my_turtle):
    my_turtle.fillcolor('grey')
    my_turtle.up()
    my_turtle.goto([0][0], [0][1])
    my_turtle.down()
    my_turtle.begin_fill()
    my_turtle.goto(points[1][0], points[1][1])
    my_turtle.goto(points[2][0], points[2][1])
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle.end_fill()

def main():
    my_turtle = turtle.Turtle()
    my_win = turtle.Screen()
    my_points = [[-100, -50], [0, 100], [100, -50]]

    draw_mount(my_points, my_turtle)
    my_win.exitonclick()

main()