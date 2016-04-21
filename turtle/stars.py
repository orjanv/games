from turtle import *
from random import *

# Tutorial found at http://kodeklubben.github.io/python/stjerner_og_galakser/stjerner_og_galakser.html
# Read more about turtle at https://docs.python.org/3.1/library/turtle.html

def RandomPosition():
    penup()
    posx = randint(-500, 500)
    posy = randint(-300, 300)
    setpos(posx, posy)
    pendown()

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
    RandomPosition()
    for star in range(numberofstars-1):
        DrawStar(randint(5, 10), "White")
        pendown()
        left(randint(-110, 110))
        forward(randint(20, 50))
    DrawStar(randint(5, 10), "White")

def DrawGalaxy(numberofstars):
    starcolors = ["White","LightBlue","Pink"]
    RandomPosition()
    for star in range(numberofstars):
        penup()
        left(randint(-200, 200))
        forward(randint(2, 15))
        pendown()
        #DrawStar(2, choice(starcolors))
        dot(2, choice(starcolors))

def WriteTitle(text):
    color("White")
    penup()
    setpos(300, 300)
    pendown()
    write (text, font = ('Times New Roman', 28, 'bold'))
    penup()

speed(0)
bgcolor("#000316")
hideturtle()

# Write title text
#WriteTitle("My sky!")

# Draw 50 random stars
for i in range(50):
    RandomPosition()
    DrawStar(randint(5, 25), "White")

# Draw 5 constellations
for constellation in range(5):
    DrawConst(randint(4, 7))

# Draw 4 small galaxies, each with 40 stars
for galaxy in range(4):
    DrawGalaxy(40)

done()
