#!/usr/bin/env python3
# script to demonstrate mod10 ciphertext - key = message
# by vjek, 20200426
###
from getpass import getpass
import random,hashlib,sys

def getphrase():
    #get sha512 of passphrase, use it as rand seed to generate OTP of any length
    #if you wanted true OTP, add ISO 8601 metric date to seed value
    #this permits arbitrary encryption and decryption based on date & passphrase
    passphrase = getpass("Passphrase:")
    if len(passphrase) < 16:
        print("Passphrase too short, enter at least 16 characters.")
        exit()
    hashphrase = hashlib.sha512(passphrase.encode('utf-8')).hexdigest()
    return hashphrase

def make_custom_dict(rand1):
    #use 00-99 values to map a-zA-Z0-9.. and create custom dictionary for mod10
    # instead of 01 = a and 26=z, the assignment will vary procedurally
    x=0
    my_dict={}
    dictionary = list(range(0,99))
    letters = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[]\{}|;':",./<>? \n'''
    rand1.shuffle(dictionary) #this shuffle will be procedural based on rand1 seed
    for letter in letters:
        my_dict[letter]="%02d" % dictionary[x]
        x=x+1
    return my_dict

def mod10(num): #this function will discard the tens place of a given two digit number
    num %= 10
    return num

#first, get the hash of a passphrase, as a random seed
hashphrase = getphrase()
rand1=random.Random()
rand1.seed(hashphrase) #use the hashed passphrase as seed
cust_dict=make_custom_dict(rand1)
#reverse the dict to lookup numbers -> letters
cust_dict = dict(zip(cust_dict.values(),cust_dict.keys()))

#take input
print("Enter the message to decrypt, up to 2048 bytes per line. End with newline + ctrl-d: ")
ciphertext1=sys.stdin.read().rstrip()
ciphertext1=ciphertext1.replace('\n','')
s_len=len(ciphertext1)

#generate the procedural OTP key
key1=''
for a in range(0,s_len):
    key1 += str(rand1.randint(0,9)) #create OTP key of message length

#perform mod10 math on ciphertext & key
ciph1=''
for a in range(0,s_len):
    m1=int(ciphertext1[a])
    k1=int(key1[a])
    ciph1 += str(mod10(m1-k1)) #mod10 message - key

#apply procedural dictionary on result
output=''
for a in range(0,s_len,2):
    try:
        output += cust_dict[ciph1[a:a+2]]
    except:
        pass
print(output)
