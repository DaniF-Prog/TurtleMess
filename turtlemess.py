import turtle
import time
import random

it = input('enter # of iterations: ')

greg = turtle.Turtle()
lisa = turtle.Screen()

g = 0

while g < it:
    g+=1

    bi = random.randint(0, 1)  

    if bi == 0:
        greg.penup()
    elif bi == 1:
        greg.pendown()
    
    wi = random.randint(1, 10)
    greg.width(wi)

    re = random.uniform(0, 1)
    gr = random.uniform(0, 1)
    bu = random.uniform(0, 1)
    greg.color(re, gr, bu)

    rd = random.uniform(0, 1)
    gn = random.uniform(0, 1)
    bl = random.uniform(0, 1)
    greg.pencolor(rd, gn, bl)

    rb = random.uniform(0, 1)
    gb = random.uniform(0, 1)
    bb = random.uniform(0, 1)
    lisa.bgcolor(rb, gb, bb)

    dist = random.randint(-100, 100)
    ang = random.randint(0, 359)
    greg.left(ang)
    greg.forward(dist)

lisa.exitonclick()
