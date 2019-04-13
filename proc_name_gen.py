#!/usr/bin/env python3
# This script produces a list of names based on either a fixed value seed, or a seed
# value provided on the command line as arg1.  A name is chosen out of the list, procedurally
# and both the list of names and the one chosen will be the same, by seed value.
# Typically, the names created are roughly pronounceable in English.
# 
# Sample output is:
#
# :./proc-name-gen.py 10
# ['Tubeso', 'Cuti', 'Pare', 'Rilohi', 'Sesu', 'Xak', 'Mupe', 'Rodunu', 'Reca', 'Yawag', 'Yefas', 'Poro', 'Guvef', 'Mezeho', 'Rebuc', 'Kaloq'] 16 Xak 5
# 
# :./proc-name-gen.py 2
# ['Dih', 'Yeyax', 'Zoviwo', 'Bis', 'Ruhuhe', 'Hih', 'Vuhor', 'Pohos', 'Lovupo', 'Xusok', 'Yiti', 'Metupu', 'Befax', 'Xefug', 'Jara', 'Pekad', 'Bab', 'Gehub', 'Kec', 'Yamit', 'Suyal', 'Tedi', 'Sev', 'Vigili', 'Wec', 'Geh', 'Zevake', 'Lax'] 28 Befax 12
###
import random,sys,string


def generate_name(length):
    VOWELS = "aeiou"
    #if you don't sort this join below , the set() - set() returns a random jumble.
    CONSONANTS = "".join(sorted(set(string.ascii_lowercase) - set(VOWELS)))
    name = ""
    for i in range(length): #this length was chosen procedurally
        if i % 2 == 0: #if even, place a consonant
            name += rand1.choice(CONSONANTS)
        else: #otherwise, place a vowel
            name += rand1.choice(VOWELS)
    return name

def create_name(): #function to pick name length
    min_name_length=3 #names can be short
    max_name_length=7 #or long.
    inval=ord(get_next_rand())
    name_length = int(mapFromTo(inval,0,255,min_name_length,max_name_length)) #pick a length from randint->range
    rand_name = generate_name(name_length) #get the name from the generator
    return rand_name

def get_next_rand(): #get the next deterministic value from the stream
    return chr(rand1.randint(0,255)) #return the next byte as char

def mapFromTo(x,a,b,c,d): #inval,start1,end1,start2,end2 for range translation
    y=(x-a)/(b-a)*(d-c)+c #most often used by me to translate 0,255 to a smaller range.
    return y #as a float; could be an int, but we may use this function differently elsewhere

seed1=8675309 #a _completely_ random seed value..
if sys.argv[1:]: #but if there is one provided
    seed1 = int(sys.argv[1]) #use that instead

rand1=random.Random() #create a new .Random intance
rand1.seed(seed1) #and make it deterministic/procedural, as in, the output will be the same

name_storage=[]
number_of_names=ord(get_next_rand()) #pick how many to generate
for a in range(number_of_names): #name generation loop
    name_storage += [(create_name().title())] #store them;first letter capitalized.
    inval=ord(get_next_rand())
    name_to_pick=int(mapFromTo(inval,0,255,0,number_of_names)) #use rand range to pick # of names
#we're at the end, so print out the list of names, number of names, a random name, and it's index
print(name_storage,len(name_storage),name_storage[name_to_pick],name_to_pick)
