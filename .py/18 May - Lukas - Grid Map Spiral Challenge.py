# ------------------------------------------
# 
# 	Project:      Grid Map Spiral Challenge
#	Author:       Lukas Krampitz    
#	Created:      18 May 2021
#	Description:  Have the robot drive around the grid drawing a spiral
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

#Move the VEX robot by a grid unit
def driveGrid(numMove):
    drivetrain.drive_for(FORWARD, 200 * numMove, MM)

#Move the first element in a List to the end
def cycleList(aList):

    #brain.print("\nIn: " + str(aList))

    tempVal = aList[0] #save the first value
    aList.append(tempVal) #add it to the back
    aList.pop(0) #remove it from the front

    #brain.print("\nOut: " + str(aList))
    return aList

def level1():

    #get the pen ready
    pen.move(DOWN)
    pen.set_pen_color(BLACK)

    #make the first move (the first line segment is repeated 1 extra time)
    driveGrid(9)
    drivetrain.turn_for(RIGHT, 90, DEGREES) 

    #go through the differnt lengths the bot needs to grive
    for i in range(9 , 0, -1):

        #drive that legnth 2 times
        for j in range(0,2):

            driveGrid(i)
            drivetrain.turn_for(RIGHT, 90, DEGREES)

def level2():

    #list of pen colours
    colours = [BLACK, RED, BLUE, GREEN]

    pen.move(DOWN)  #start drawing on the ground

    pen.set_pen_color(colours[0]) #get the first colour
    colours = cycleList(colours) #move to the next colour

    driveGrid(9)
    drivetrain.turn_for(RIGHT, 90, DEGREES) 

    #go through the differnt lengths the bot needs to grive
    for i in range(9 , 0, -1):

        #drive that legnth 3 times
        for j in range(0,2):

            #change up the colour for the next segment
            pen.set_pen_color(colours[0])
            colours = cycleList(colours)

            driveGrid(i)
            drivetrain.turn_for(RIGHT, 90, DEGREES)

def level3():

    colours = [BLACK, RED, BLUE, GREEN]

    pen.move(DOWN)   

    pen.set_pen_color(colours[0])
    colours = cycleList(colours)

    driveGrid(9)
    drivetrain.turn_for(RIGHT, 90, DEGREES) 

    #go through the differnt lengths the bot needs to grive
    for i in range(9 , 0, -1):

        #drive that legnth 2 times
        for j in range(0,2):

            pen.set_pen_color(colours[0])
            colours = cycleList(colours)

            driveGrid(i)
            drivetrain.turn_for(RIGHT, 90, DEGREES)
    

    pen.move(UP)  

    drivetrain.turn_to_heading(0, DEGREES)

    for i in range(1 , 10):
        #drive that legnth 2 times
        for j in range(0,2):

            driveGrid(i)
            drivetrain.turn_for(LEFT, 90, DEGREES)
    driveGrid(9)
    
# Add project code in "main"
def main():
    init()

    level3()

# VR threads — Do not delete
vr_thread(main())
