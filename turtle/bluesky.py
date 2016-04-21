from turtle import *
from random import *

bgcolor("SkyBlue")

def RandomPosition():
    penup()
    posx = randint(-500, 500)
    posy = randint(-200, 300)
    setpos(posx, posy)
    pendown()
    
def seagull(gullsize):
    color("Grey")
    pensize(2)
    penup()
    setheading(90)
    RandomPosition()
    pendown()
    right(135)
    forward(gullsize)
    left(90)
    forward(gullsize)
    penup()

def skies(size):
    color("White")
    RandomPosition()
    setheading(360)
    pendown()
    begin_fill()
    circle(size,180)
    setheading(90)
    circle(size*1.33,180)
    setheading(180)
    circle(size,180)
    forward((size*1.33)*2)
    left(90)
    forward(size*2)
    end_fill()
    penup()

def thesun():
    color("Yellow")
    RandomPosition()
    pendown()
    begin_fill()
    circle(70)
    end_fill()
    penup()

def rainbow(size):
    penup()
    colors = ["#FF0000", "#FFA500", "#FFFF00", "#00FF00",
              "#0000FF", "#4B0082", "#8F00FF"]
    posx = randint(-400, 400)

    for c in colors:
        color(c)
        setpos(posx, -370)
        setheading(90)
        pendown()
        begin_fill()
        circle(size, 180)
        left(90)
        forward(10)
        left(90)
        circle(-size+10, 180)
        left(90)
        forward(10)
        end_fill()
        penup()

        posx = posx-10
        size = size-10

def house(x, y, h, w, col):
    color(col)
    pencolor("Black")
    setpos(x, y)
    setheading(90)
    pendown()
    begin_fill()
    for i in range(2):
        forward(h)
        right(90)
        forward(w)
        right(90)
    end_fill()
    penup()


setup(1200, 900)
speed(0)
hideturtle()

# Draw the sun
thesun()

# Draw houses
'''
x = randint(-400, 400)
y = -370
h = 80
for i in range(7):
    house(x, y, h, 40, "Grey")
    for window in range(3):
        y = y + 20
        house(x+10, y, 15, 20, "Black")
    y = -370
    x = x + 40
    h = h + randint(-30, 30)
'''

# Draw a rainbow
rainbow(300)

# Draw seven skies in random sizes
for sky in range(7):
    size = randint(10, 40)
    skies(size)

# Draw 20 seagulls
for gull in range(20):
    gullsize = randint(5, 25)
    seagull(gullsize)

done()
