from turtle import *
from random import *
import time

HUS_FARGER = ["#363432", "#196774", "#90A19D", "#F0941F", "#BD2A2E", "#3B3936", "#889C9B", "#486966"]
VINDU_FARGER = ["#F2F2F2", "#202022"]
husbredde_liste = [50, 70, 90, 110, 130] # liste over forskjellige husbredder
antall = 14 # int(skjerm_bredde/husbredde_liste[-1]) # regne ut maks antall etter skjermbredde

skjerm_bredde = 1700
skjerm_hoyde = 1000
setup(skjerm_bredde, skjerm_hoyde)
bgcolor("SkyBlue")
tracer(0) # sett til 0 for å tegne umiddelbart, da betyr speed() ingenting
speed('fastest')
hideturtle()


def bakgrunn(x, y, h, w, col):
    # Tegne firkant-funksjon
    penup()
    color(col)
    pencolor(col)
    setpos(x, y)
    #setheading(90)
    pendown()
    begin_fill()
    for i in range(2):
        forward(h)
        right(90)
        forward(w)
        right(90)
    end_fill()
    penup()
    
def firkant(x, y, h, w, col):
    # Tegne firkant-funksjon
    penup()
    color(col)
    pencolor(col)
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

def DrawHouses(no_houses):
    # Bygg husene
    x = (skjerm_bredde / -2) + 100 # begynn å tegne her
    for hus in range(no_houses + 1):
        b = choice(husbredde_liste) # trekk en tilfeldig husbredde
        y = -500 # hold deg på samme linje
        h = randrange(60, 600, 30) + 10 # tilfedig høyde, men tilpasset vindustørrelser, må gå opp i 30 (20+10)
        firkant(x, y, h, b, choice(HUS_FARGER))
        for window in range(int(h/30)): # regn ut antall vindu å tegne inn
            for i in range(10, b, 20):
                firkant(x + i, y + 10, 20, 10, choice(VINDU_FARGER))
            y = y + 30 # avstand til neste etasje
        x = x + b + 1 # mellomrom til neste hus

def RandomPosition():
    penup()
    posx = randint(round(skjerm_bredde/2*-1), round(skjerm_bredde/2))
    posy = randint(round(skjerm_hoyde/4*-1), round(skjerm_hoyde/2))
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
    colors = ["#FF0000", "#FFA500", "#FFFF00", "#00FF00", "#0000FF", "#4B0082", "#8F00FF"]
    posx = randint(-400, 400)
    posy = -500
    for c in colors:
        color(c)
        setpos(posx, posy)
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


def main():
    # draw a background
    bakgrunn(skjerm_bredde/2*-1, skjerm_hoyde/2, skjerm_bredde, skjerm_hoyde, 'SkyBlue')
    
    # Draw the sun
    thesun()

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

    DrawHouses(antall)

    # Save the art as an image and big enough
    filename = f'daysky_{time.strftime("%Y-%m-%d_%H-%M-%S")}.eps'
    getcanvas().postscript(file=filename, colormode='color', width=skjerm_bredde, height=skjerm_hoyde)

    #exitonclick()


if __name__ == '__main__':
    main()

