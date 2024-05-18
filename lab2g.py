#!/usr/bin/env python3
'''
Author:  LAU Chi Kong
Author ID:  cklau9
Date Created:  2024/05/17

'''
import sys

# Assign the value of 3 to an object named timer when there are no arguments provided
if len(sys.argv) != 2:
    timer = 3 
else:
    timer = int(sys.argv[1])# Assign the value of int(sys.argv[1]) to an object named timer when one command line argument is entered
    
while timer != 0: #Set the WHILE loop stop at 0
        print(timer)
        timer = timer - 1

print('blast off!')
