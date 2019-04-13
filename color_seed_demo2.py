#!/usr/bin/env python3
# This script produces a deterministic color field
# based on either a fixed value seed, or a seed
# value provided on the command line as arg1.
# It will print out the associated RGB colors, in
# sequence, from the deterministic stream, and a char.
# It will print one full screen of a given termsize.
###
import random,os,sys,string

def print_block(fg_red=255,fg_green=255,fg_blue=255,char=" ",bg_red=0,bg_green=0,bg_blue=0): #uses 24bit terminal RGB
    out=str.format("\033[38;2;{};{};{}m\033[48;2;{};{};{}m{}"\
            ,fg_red,fg_green,fg_blue,bg_red,bg_green,bg_blue,char) #assemble string
    print(out,end='') #print the colored string (a char with \ESC codes)
    return

def reset_color(): #used to reset the \ESC codes
    print("\033[0m") # back to their defaults

def get_next_rand(): #get the next determinstic value from the stream
    return chr(rand1.randint(0,255)) #return the next byte as char

seed1=8675309 #a _completely_ random seed value..
if sys.argv[1:]: #but if there is one provided
        seed1 = int(sys.argv[1]) #use that instead

rand1=random.Random() #create a new .Random intance
rand1.seed(seed1) #and make it deterministic, as in, the output will be the same

if os.name != "posix": #this will check if this is a posix compatible environment
    print("This was meant to run under a posix OS, so it probably won't look right for you")
    os._exit(1)

ts = os.get_terminal_size() #get the terminal_size data
term_width = ts.columns #columns for width
term_length = ts.lines -3 #rows for length, subtract a bit for prompt visibility
color_storage=[] #start a new list
# print out the screen full of colors
for a in range(term_width * term_length): #number of times is W x L
    r1=ord(get_next_rand()) #red, ord() converts chr to int
    g1=ord(get_next_rand()) #green
    b1=ord(get_next_rand()) #blue
    c1=rand1.choice(string.ascii_letters) #single character
    r2=ord(get_next_rand()) #red
    g2=ord(get_next_rand()) #green
    b2=ord(get_next_rand()) #blue
    color_storage += [(r1,g1,b1,c1,r2,g2,b2)] #store the colors/chars as tuples in list
    print_block(fg_red=r1,fg_green=g1,fg_blue=b1,char=c1,bg_red=r2,bg_green=g2,bg_blue=b2) 
reset_color() #reset colors back to defaults
# we're at the end, so print out number of blocks, first block fg, char, and bg.
print(len(color_storage),term_width * term_length,color_storage[0])
