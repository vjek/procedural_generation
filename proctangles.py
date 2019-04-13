#!/usr/bin/env python3
# this script will draw 60 deterministic rectangles on a tkinter canvas
# using procedural generation so that it will be the same each time,but appear random
# this script accepts a single optional command line argument as a seed, if desired
###
from tkinter import * #this adds all to namespace, no tkinter prepend necessary<-py3
import random #this requires random.function for module use

canvas_width=canvas_height=600 #vals for square canvas size
canvas = Canvas(Tk(), width=canvas_width, height=canvas_height) #create canvas
canvas.winfo_toplevel().title("Lots of Rectangles") #name the canvas window something
canvas.pack() #create canvas instance

def random_rectangle(width,height,fill_color): #function to draw a rectangle
    x1 = rand1.randrange(width) #create random upper left
    y1 = rand1.randrange(height)
    x2 = rand1.randrange(width) #create random lower right
    y2 = rand1.randrange(height)
    canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color) #draw the rectangle

rand1=random.Random() #create soon to be un-random random instance
seed1=8675309 #a _completely_ random seed value..
if sys.argv[1:]: #but if there is one provided
        seed1 = int(sys.argv[1]) #use that instead
rand1.seed(seed1) #seed the random instance with a set value

for x in range(0,60): #loop to draw n rectangles
    randcolor = rand1.randrange(2**24) #color range 2^24, for all 16M RGB colors
    randcolor = "#%06x" % randcolor #format for #ff00ff color
    random_rectangle(width=canvas_width, height=canvas_height, fill_color=randcolor) #draw
    canvas.update() #reveal/update canvas changes
input("Press Enter to end ") #this is just here so the canvas doesn't disappear at the end
