#!/usr/bin/env python3

#Import sys module and apply the sys.argv to get input from command line
import sys


#Check if no. of arg is !=3 (script name, name & age)
if len(sys.argv) !=3:
    print('Usage: ./lab2d.py name age')
    sys.exit()

#Assign the cmd line arg. to variables (name & age)
name = sys.argv[1]
age = sys.argv[2]

#Print the message including above variables
print('Hi ' + name + ', you are ' + age + ' years old.') 