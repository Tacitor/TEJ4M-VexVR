# ------------------------------------------
# 
# 	Project:      VEXcode Project
#	Author:       VEX
#	Created:
#	Description:  VEXcode VR Python Project
# 
# ------------------------------------------

# Library imports
from vexcode import *

def init():
    #set the speed to be faster
    drivetrain.set_drive_velocity(100, PERCENT)
    drivetrain.set_turn_velocity(100, PERCENT)
    brain.clear()


def driveGrid(numMove):
    drivetrain.drive_for(FORWARD, 200 * numMove, MM)

def cycleList(aList):

    #brain.print("\nIn: " + str(aList))

    tempVal = aList[0]
    aList.append(tempVal)
    aList.pop(0)

    #brain.print("\nOut: " + str(aList))
    return aList

def driveSequ(sqeuenceSize, ordList, movList):
    for i in range(sqeuenceSize):
        if ordList[i] == X:
            drivetrain.turn_to_rotation(90, DEGREES)
        else:
            drivetrain.turn_to_rotation(0, DEGREES)       
        drivetrain.drive_for(FORWARD, movList[i], MM)

def goTo(xPos, yPos):
    curX = location.position(X, MM)
    curY = location.position(Y, MM)

    movX = xPos - curX
    movY = yPos - curY

    #check for 1D movemnt
    if (movX == 0):
        driveSequ(1, [Y], [movY])
    elif (movY == 0):
        driveSequ(1, [X], [movX])
    else:
        driveSequ(2, [X, Y], [movX, movY])

def getPos():

    curCoords = [location.position(X, MM), location.position(Y, MM)]

    return curCoords

def printArt(array):

    output = "Art\n"

    for i in range(len(array)):

        for j in range(len(array)):

            output = output + str(array[i][j]) + " "

        output = output + "\n"

    brain.print(output)

def level3():

    offChar = "0"
    onChar = "◘"
    gridSize = 7 

    global art
    art = [[offChar]]

    #create the 2D array with all 0s
    for i in range(gridSize): #have 8 rows
    
        art.append([offChar])

        #add the columns
        for j in range(gridSize):
            art[i].append(offChar)

    #add the last row
    for j in range(gridSize):
        art[gridSize].append(offChar)

    monitor_variable("art")


    #go through all the positions under the gold roofs

    #move to starting pos
    goTo(-900, 900)

    #scan the column
    for i in range(8):

        drivetrain.turn_to_heading(180, DEGREES)
        driveGrid(1)

        #scan the row
        drivetrain.turn_to_heading(90, DEGREES)
        for j in range(8):
            driveGrid(1)
            
            #check if the tile is "filled"
            if (down_eye.detect(GREEN)):
                art[i][j] = onChar

            wait(5, MSEC)
        #go back
        driveGrid(-8)

    #print the art
    printArt(art)

# Add project code in "main"
def main():
    init()

    level3()

# VR threads — Do not delete
vr_thread(main())
