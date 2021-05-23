# ------------------------------------------
# 
# 	Project:      Color Counting Algorithms Challenge
#	Author:       Lukas Krampitz
#	Created:      05 May 2021
#	Description:  Have the VEXcode VR robot detect and count coloured lines on the ground
# 
# ------------------------------------------

# Library imports
from vexcode import *

#Util function used to setup movement speeds
def init():
    #set the speed to be faster
    drivetrain.set_drive_velocity(100, PERCENT)
    drivetrain.set_turn_velocity(100, PERCENT)

#Util function to move the robot forward exactly one grid quare
def driveGrid(numMove):
    drivetrain.drive_for(FORWARD, 200 * numMove, MM)

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
        #move the robot by the desired grid spaces 
        driveGrid(movList[i])

#Accepts the same parameters as driveSequ(), but reverses the order and direction of the sequence
def driveSequRev(sqeuenceSize, ordList, movList):
    newOrdList = [ordList[sqeuenceSize - 1]]
    newMovList = [-movList[sqeuenceSize - 1]]

    #flip the sequence
    for i in range(sqeuenceSize - 1):
        newOrdList.append(ordList[sqeuenceSize - 2 - i])
        newMovList.append(-movList[sqeuenceSize - 2 - i])

    driveSequ(sqeuenceSize, newOrdList, newMovList)

def level1():
    #start driving forward
    drivetrain.drive(FORWARD)

    #while driving forward cound the green lines beneath the bot
    greenCount = 0
    while greenCount < 2:
        if down_eye.detect(GREEN):
            greenCount = greenCount + 1

        wait(120,MSEC)

    #when 2 greens have been detected the flow breaks out of the loop and stops the bot
    drivetrain.stop()

def level2():
    #similar to level 1 but now detects all colours
    drivetrain.drive(FORWARD)


    currentColour = "none"
    #drive to the end of the course
    while location.position(Y, MM) < 900:
        #check the line's colour
        if down_eye.detect(GREEN) and not currentColour == "green":
            currentColour = "green"
            brain.print("green\n")  
        elif down_eye.detect(RED) and not currentColour == "red":
            currentColour = "red"
            brain.print("red\n")  
        elif down_eye.detect(BLUE) and not currentColour == "blue":
            currentColour = "blue"
            brain.print("blue\n")
        elif down_eye.detect(NONE) and not currentColour == "none":
            currentColour = "none"     
        

        wait(10,MSEC)

    drivetrain.stop()

def level3():
    #same as level 2, but now keep track of the colours counted
    drivetrain.drive(FORWARD)

    #temp val storage
    currentColour = "none"
    #accumulators
    total = 0
    red = 0
    blue = 0
    green = 0
    #drive to the end of the course
    while location.position(Y, MM) < 900:
        if down_eye.detect(GREEN) and not currentColour == "green":
            currentColour = "green"
            green+=1 #increment by 1
        elif down_eye.detect(RED) and not currentColour == "red":
            currentColour = "red"
            red+=1
        elif down_eye.detect(BLUE) and not currentColour == "blue":
            currentColour = "blue"
            blue+=1
        elif down_eye.detect(NONE) and not currentColour == "none":
            currentColour = "none"   
            total+=1  
        

        wait(10,MSEC)

    drivetrain.stop()

    #display the output
    brain.print("Total RGB lines:" + str(total) + "\n")
    brain.print("Total red lines:" + str(red) + "\n")
    brain.print("Total green lines:" + str(green) + "\n")
    brain.print("Total blue lines:" + str(blue) + "\n")


# Add project code in "main"
def main():
    init()

    level2()



# VR threads — Do not delete
vr_thread(main())
