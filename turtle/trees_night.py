#!/usr/bin/env python3
#-*- coding:utf-8 -*-
from turtle import *
from random import randint, choice

def RandomTreePosition():
    penup()
    posx = randint(-550, 550)
    posy = randint(-400, -200)
    setpos(posx, posy)


def RandomStarPosition():
    penup()
    posx = randint(-600, 600)
    posy = randint(-100, 450)
    setpos(posx, posy)


def DrawStar(size, starcolor):
    color(starcolor)
    pendown()
    begin_fill()
    for line in range(5):
        left(144)
        forward(size)
    end_fill()
    penup()


def DrawConst(numberofstars):
    RandomStarPosition()
    for star in range(numberofstars-1):
        DrawStar(randint(5, 10), "White")
        pendown()
        left(randint(-110, 110))
        forward(randint(20, 50))
    DrawStar(randint(5, 10), "White")


def DrawGalaxy(numberofstars):
    starcolors = ["White","LightBlue","Pink"]
    RandomStarPosition()
    for star in range(numberofstars):
        penup()
        left(randint(-200, 200))
        forward(randint(2, 15))
        pendown()
        dot(2, choice(starcolors))


def DrawTree(size, treecolor):
    color(treecolor)
    pendown()
    begin_fill()
    left(180)

    # opp på venstre side
    ul = size
    ur = size+(size/5)*2
    for i in range(4):
        forward(ul)
        right(135)
        forward(ur)
        left(135)
        ul -= size/5
        ur -= size/5

    # ned igjen på høyre side
    dr = size-(size/5)
    dl = size-(size/5)*3
    for i in range(4):
        left(135)
        forward(dr)
        right(135)
        forward(dl)
        dr += size/5
        dl += size/5

    end_fill()
    penup()

    print(pos())
    # stammen
    forward(size/2)
    left(180)
    pendown()
    begin_fill()
    color("#7c6757")
    for i in range(2):
        forward(size/4)
        right(90)
        forward(size/2)
        right(90)

    end_fill()
    penup()


# some setup
setup(1200, 900)
hideturtle()
speed(0) # move quick
delay(0) # Make turtle draw instant
bgcolor("#232629")

# Draw random stars
for i in range(50):
    RandomStarPosition()
    DrawStar(randint(3, 15), "White")


# Draw 4 small galaxies, each with 40 stars
for galaxy in range(4):
    DrawGalaxy(40)

# Draw 5 constellations
for constellation in range(5):
    DrawConst(randint(4, 7))

# Draw trees
setheading(0)
tree_colors = ["#2a936d", "#4acc9a", "#39b28a"]
for i in range(10):
    RandomTreePosition()
    treesize = randint(30,120)
    DrawTree(treesize, choice(tree_colors))


done()

