# ------------------------------------------
# 
# 	Project:      Hidden Pixel Art Challenge
#	Author:       Lukas Krampitz    
#	Created:      19 May 2021
#	Description:  Have the robot drive uderneath a roof covering a pattern on the floor. Use the bot to scan the floor and read out the pixel art.
# 
# ------------------------------------------

# Library imports
from vexcode import *

def init():
    #set the speed to be faster
    drivetrain.set_drive_velocity(100, PERCENT)
    drivetrain.set_turn_velocity(100, PERCENT)
    brain.clear()

#Move the VEX robot by a grid unit
def driveGrid(numMove):
    drivetrain.drive_for(FORWARD, 200 * numMove, MM)

#cycle through a List. Move the first element to the end of the List
def cycleList(aList):

    #brain.print("\nIn: " + str(aList))

    tempVal = aList[0] #store the first value
    aList.append(tempVal) #move it
    aList.pop(0) #remove the original occurence of it

    #brain.print("\nOut: " + str(aList))
    return aList

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

    #check for 1D movemnt
    if (movX == 0):
        driveSequ(1, [Y], [movY])
    elif (movY == 0):
        driveSequ(1, [X], [movX])
    else:
        driveSequ(2, [X, Y], [movX, movY])

#get the current position fot he robot
def getPos():

    curCoords = [location.position(X, MM), location.position(Y, MM)]

    return curCoords

#Util function used to display the result of scaning the 8x8 art grid
def printArt(array):

    output = "Art\n"
    #loop through the rowss
    for i in range(len(array)):
        #add the row elements
        for j in range(len(array)):
            #add the the output string
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
