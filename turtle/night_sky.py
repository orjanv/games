from turtle import *
from random import *
import time

HUS_FARGER = ["#363432", "#196774", "#90A19D", "#F0941F", "#BD2A2E", "#3B3936", "#889C9B", "#486966"]
VINDU_FARGER = ["#F2F2F2", "#202022"]

# Litt oppsett
skjerm_bredde = 1700
skjerm_hoyde = 1000
setup(skjerm_bredde, skjerm_hoyde)
tracer(0) # sett til 0 for å tegne umiddelbart, da betyr speed() ingenting
speed('fastest')
bgcolor("#000316")
husbredde_liste = [50, 70, 90, 110, 130] # liste over forskjellige husbredder
antall = 14 # int(skjerm_bredde/husbredde_liste[-1]) # regne ut maks antall etter skjermbredde
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

def DrawStar(size, starcolor):
    color(starcolor)
    pendown()
    begin_fill()
    for line in range(5):
        left(144)
        forward(size)
    end_fill()
    penup()

def DrawConstallation(numberofstars):
    RandomPosition()
    for star in range(numberofstars-1):
        dot(randint(5, 10), "White")
        pendown()
        left(randint(-110, 110))
        forward(randint(20, 50))
    dot(randint(5, 10), "White")

def DrawGalaxy(numberofstars):
    starcolors = ["White","LightBlue","Pink"]
    RandomPosition()
    for star in range(numberofstars):
        penup()
        left(randint(-200, 200))
        forward(randint(2, 15))
        pendown()
        dot(2, choice(starcolors))


def main():
    # draw a background
    bakgrunn(skjerm_bredde/2*-1, skjerm_hoyde/2, skjerm_bredde, skjerm_hoyde, '#000316')


    # Draw 50 random stars
    for i in range(50):
        RandomPosition()
        DrawStar(randint(5, 25), "White")

    # Draw 5 constellations
    for constellation in range(5):
        DrawConstallation(randint(4, 7))

    # Draw 4 small galaxies, each with 40 stars
    for galaxy in range(4):
        DrawGalaxy(40)

    DrawHouses(antall)
    
    # Save the art as an image and big enough
    filename = f'nightsky_{time.strftime("%Y-%m-%d_%H-%M-%S")}.eps'
    getcanvas().postscript(file=filename, colormode='color', width=skjerm_bredde, height=skjerm_hoyde)

    #exitonclick()


if __name__ == '__main__':
    main()

