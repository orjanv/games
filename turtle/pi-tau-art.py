#!/usr/bin/env python
#-*- coding:utf-8 -*-
import time
import sys
from turtle import *

'''
    pi-tau-art.py - Copyright 2019 Ørjan Hoyd H. Vøllestad <hoyd@earth>
    
    SCRIPT TO DRAW Pi AND Tau ART FROM THEIR DECIMALS USING TURTLE
    
    For each decimal in pi or tau, draw a pixel square with the distinct color 
    matching the decimal value:

    #e6194b - 0
    #f58231 - 1
    #ffe119 - 2
    #bfef45 - 3
    #3cb44b - 4
    #42d4f4 - 5
    #4363d8 - 6
    #911eb4 - 7
    #f032e6 - 8
    #a9a9a9 - 9

    Then, move forward two times the value and turn left some degrees 
    also times the value of the decimal.
'''

def drawSquare(square_size, square_color, canvas):
    ''' The function used to draw the square and fill with color
    '''
    canvas.color(square_color)
    canvas.pendown()
    canvas.begin_fill()
    for line in range(4):
        canvas.left(90)
        canvas.forward(square_size)
    canvas.end_fill()
    canvas.penup()
    
def readDecimals(decimalfile):
    ''' Open textfile with pi digits and create a list of the digits
    '''
    with open(decimalfile, 'r') as file:
        data = file.read().replace('\n', '')
    pi_digits = [int(d) for d in str(data)]
    return pi_digits

def piArt(digits, canvas, color_list, square_size, initial_angle):
    ''' A function to call the square drawing, forward and turn according
        to the decimal value.
    '''
    canvas.penup()
    # Move to a good starting point before drawing
    # ~ canvas.goto(1500,-2000) # good position for pi100k
    # ~ canvas.goto(2500,-2000) # good position for pi10k
    # ~ canvas.goto(500,-1800) # good position for euler10k
    canvas.goto(2000,-3000) # good position for tau100k
    
    for idx, val in enumerate(digits):
        posx,posy = canvas.pos()
        drawSquare(square_size, str(color_list[val]), canvas)
        canvas.forward(square_size*val)
        canvas.left(initial_angle*val)

def main():
    ''' The main function where some variables are set and the drawing starts
    '''
    # Set some variables for the canvas and drawing
    ten_colors = ['#e6194b', '#f58231', '#ffe119', '#bfef45', '#3cb44b', \
        '#42d4f4', '#4363d8', '#911eb4', '#f032e6', '#a9a9a9']
    canvas_width = 5000
    canvas_height = 5000
    square_size = 2
    initial_angle = 90

    # DO SOME TURTLE SETUP
    t = Turtle() # Set up a turtle instance with a screen and a canvas
    t.screen.setup(canvas_width, canvas_height) # Setting up the window "screen" size
    t.screen.screensize(canvas_width, canvas_height, 'White') # Not needed for the canvas output, just for viewing
    t.hideturtle() # Don't show the turtle on screen
    t.tracer(0) # Make turtle draw instant

    # Draw the art with all the digits from given file
    try:
        piArt(readDecimals(sys.argv[1]), t, ten_colors, square_size, initial_angle)
    except:
        print "You didn't spesify an input file..\n"

    # Save the art as an image and big enough
    filename = "pi_art-" + time.strftime("%Y-%m-%d_%H-%M-%S") + ".eps"
    getcanvas().postscript(file=filename, colormode='color', width=canvas_width, height=canvas_height)

    exitonclick() # Close the drawing window when tapping or clicking on it

if __name__ == '__main__':
    main()
