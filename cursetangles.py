#!/usr/bin/env python3
# this script will draw deterministic rectangles on a curses screen/window
# using procedural generation so that it will be the same each time,but appear random
# this script accepts a single optional command line argument as a seed, if desired
# the location, shape and color of the rectangles is unique per seed.  A short delay
# is in place so the observer can watch the rectangles being drawn.
###
import os,random,curses,sys
from time import sleep

def random_rectangle(stdscr,width,height,color_pair): #function to draw a rectangle
    xsize = rand1.randrange(width) #random size for box
    ysize = rand1.randrange(height)
    x1 = rand1.randrange(width-xsize) #create random upper left
    y1 = rand1.randrange(height-ysize)
    area = (xsize * ysize) #how big is the window?
    pos_string=area * " " #create the right amount of spaces to fill the window
    curr_win=stdscr.subwin(ysize,xsize,y1,x1) #use newwin for reused window, subwin for new/overtop
    try:
        curr_win.addstr(0, 0, pos_string, curses.color_pair(color_pair)) #fill in subwin with color
    except curses.error as e: #handles the bottom right corner exception due to _WRAPPED flag
        pass #and ignore it, and continue
    stdscr.refresh() #update the screen
    sleep(0.01) #a bit of a delay so we can see it happening
    return

def draw_rectangles(stdscr):
    curses.use_default_colors() #need this for 256 color support
    height, width = stdscr.getmaxyx() #get screensize
    num_list = list(range(1,curses.COLORS)) #create a list of all color possibilities
    rand1.shuffle(num_list) #shuffle the list, procedurally
    for x in range(1,len(num_list)): #loop to draw n rectangles, one per color
        curses.init_pair(x, 255, num_list[x]) #change background color to a color in the list
        random_rectangle(stdscr=stdscr, width=width, height=height, color_pair=x) #draw
    stdscr.getch() #wait for keypress
    return

os.environ['TERM'] = 'xterm-256color' #set this temporarily so the script will work
rand1=random.Random() #create soon to be un-random random instance
seed1=8675309 #a _completely_ random seed value..
if sys.argv[1:]: #but if there is one provided
        seed1 = int(sys.argv[1]) #use that instead
rand1.seed(seed1) #seed the random instance with a set value

curses.wrapper(draw_rectangles) #start everything, and exit gracefully when done
