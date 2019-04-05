#!/usr/bin/env python3
# This script produces a deterministic color field
# based on either a fixed value seed, or a seed
# value provided on the command line as arg1.
# It will print out the associated RGB colors, in
# sequence, from the deterministic stream.
# It will print one full screen of a given termsize
###
import random,os,sys

def print_color(red=0,green=0,blue=0): #uses 24bit terminal RGB
    out='' #start of output string
    out+=(str.format("\033[48;2;{};{};{}m ",red,green,blue)) #assemble string
    print(out,end='') #print the colored string (a space with \ESC codes)
    return

def reset_color(): #used to reset the \ESC codes
    print("\033[0m") # back to their defaults

def get_next_rand(): #get the next determinstic value from the stream
    return rand1.randint(0,9) #return the next single digit number

seed1=8675309 #a _completely_ random seed value..
if sys.argv[1:]: #but if there is one provided
        seed1 = int(sys.argv[1]) #use that instead

rand1=random.Random() #create a new .Random intance
rand1.seed(seed1) #and make it deterministic, as in, the output will be the same

if os.name != "posix": #this will check if this is a posix compatible environment
    print("This was meant to run under a posix OS, so it probably won't look right for you")
    os._exit(1)

ts = os.get_terminal_size() #get the termina_size data
term_width = ts.columns #columns for width
term_length = ts.lines - 3 #rows for length, subtract a bit for prompt visibility
# print out the screen full of colors
for a in range(term_width * term_length): #number of times is W x L
    r1=int((( get_next_rand() / 10 )* 255)) #red
    g1=int((( get_next_rand() / 10 )* 255)) #green
    b1=int((( get_next_rand() / 10 )* 255)) #blue
    print_color(red=r1,green=g1,blue=b1) #print an ansi RGB color block
reset_color() #reset colors back to defaults
