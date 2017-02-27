#!/usr/bin/env python

#program info
__title__ = "Screen Size Calculator"
__description__ = """This program calculates the dimensions of a screen
                     based on the diameter and the ratio of the screen."""
__author__ = "Peter Sz."
__licence__ = "GPLv3"
__version__ = "0.1"

#modules
import math
import time

#static values
inch = 2.54
query = "Input screen diameter in inches.\n"


def welcome():
    #Welcome message
    print "Welcome to %s v%s." % (__title__, __version__)
    time.sleep(1)
    print "Directions:"
    time.sleep(1)
    print "Enter values using your keyboard and press ENTER to submit.\n"
    time.sleep(1)
 
def cont():
    #Asks if the user wants to continue (Y/n).
    print
    answer = raw_input("Do you want another calculation? (Y/n)")
    if answer.lower() == "y" or answer == "":
        selectratio()
    elif answer.lower() == "n":
        exit()
    else:
        cont() 

def fourthree():
    print
    c = float(raw_input(query))
    x = c / 5
    print "Screen size:\n%s cm\n%s cm" % (round(x * 4 * inch, 1), 
                                           round(x * 3 * inch, 1))
    cont()

def sixteennine():
    print
    c = float(raw_input(query))
    x = c / math.sqrt(337)
    print "Screen size:\n%s cm\n%s cm" % (round(x * 16 * inch, 1), 
                                           round(x * 9 * inch, 1))
    cont()

def selectratio():
    print "Select screen ratio:"
    print "a) 4:3 screen"
    print "b) 16:9 screen"
    time.sleep(1)
    ratio = raw_input()
    if ratio.lower() == "a":
        fourthree()
    elif ratio.lower() == "b":
        sixteennine()
    else:
        selectratio()
 
#start program
welcome()
selectratio()
