# ------------------------------------------
# 
# 	Project:      Storm the Castle Challenge
#	Author:       Lukas Krampitz    
#	Created:      07 May 2021
#	Description:  Drive around and destroy castles
# 
# ------------------------------------------

# Library imports
from vexcode import *

#Util function used to setup movement speeds and clear chat
def init():
    #set the speed to be faster
    drivetrain.set_drive_velocity(100, PERCENT)
    drivetrain.set_turn_velocity(100, PERCENT)
    brain.clear()

#Moves the robot in a sequence of linear paths.
#Accepts the number of moves
#The axis patternt the robot will take
#And the distances the robot will drive 
def driveSequ(sqeuenceSize, ordList, movList):
    #go through the secuence given
    for i in range(sqeuenceSize):
        #set the rotation based on X or Y axis movement
        if ordList[i] == X:
            drivetrain.turn_to_rotation(90, DEGREES)
        else:
            drivetrain.turn_to_rotation(0, DEGREES)       
        #move the robot by the desired amounts
        drivetrain.drive_for(FORWARD, movList[i], MM)

#move the robot to a specific set of co-ordinates
def goTo(xPos, yPos):
    curX = location.position(X, MM)
    curY = location.position(Y, MM)

    movX = xPos - curX
    movY = yPos - curY

    driveSequ(2, [X, Y], [movX, movY])

#target specific building on the static map
def level1():
    goTo(-900, 800)
    goTo(900, 800)
    goTo(700, -800)
    goTo(0, 100)

def level2():
    goTo(-600, 0) #get around the bottom corner
    goTo(-700, 1000) #remove the right saide
    goTo(-600, 0) #reposition
    goTo(-900, 1000) #remove the left side

#for the dynamic maps
def level3():

    xPos = location.position(X, MM)
    yPos = location.position(Y, MM)

    #start removal loop
    while True:
        #get in position
        goTo(0, -1000)

        while location.position(Y, MM) < 1010:
            #check left
            drivetrain.turn_for(LEFT, 90, DEGREES)        
            #check if there is a building
            if (distance.get_distance(MM) < 2500):
                xPos = location.position(X, MM)
                yPos = location.position(Y, MM)
                drivetrain.drive_for(FORWARD, 1050, MM) 
                wait(100, MSEC)              
                goTo(xPos, yPos)
            #recentre
            drivetrain.turn_to_heading(0, DEGREES)

            #check right
            drivetrain.turn_to_heading(90, DEGREES)        
            #check if there is a building
            if (distance.get_distance(MM) < 2500):
                xPos = location.position(X, MM)
                yPos = location.position(Y, MM)
                drivetrain.drive_for(FORWARD, 1050, MM) 
                wait(100, MSEC)       
                goTo(xPos, yPos)
            #recentre
            drivetrain.turn_to_heading(0, DEGREES)

            if (location.position(Y, MM) < 900):
                #move forward
                drivetrain.drive_for(FORWARD, 200, MM) 
            else:
                drivetrain.drive_for(FORWARD, 10, MM) 

def level4():
    level3()


# Add project code in "main"
def main():
    init()

    level4()

# VR threads — Do not delete
vr_thread(main())
