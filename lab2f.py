#!/usr/bin/env python3
'''
Author:  LAU Chi Kong
Author ID:  cklau9
Date Created:  2024/05/17

'''
import sys

timer = int(sys.argv[1]) #Assign the value of an integer in sys.argv[1] to an object named timer

while timer != 0: #Set the WHILE loop stop at 0
    print(timer)
    timer = timer - 1
print('blast off!')
