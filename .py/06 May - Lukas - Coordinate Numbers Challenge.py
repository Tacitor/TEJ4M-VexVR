# ------------------------------------------
# 
# 	Project:      Coordinate Numbers Challenge
#	Author:       Lukas Krampitz
#	Created:      06 May 2021
#	Description:  Have the VEXcode VR robot move to grid squares and calculate their number 
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
        #move the robot by the desired amounts
        drivetrain.drive_for(FORWARD, movList[i], MM)

#Accepts the same parameters as driveSequ(), but reverses the order and direction of the sequence
def driveSequRev(sqeuenceSize, ordList, movList):
    newOrdList = [ordList[sqeuenceSize - 1]]
    newMovList = [-movList[sqeuenceSize - 1]]

    #flip the sequence
    for i in range(sqeuenceSize - 1):
        newOrdList.append(ordList[sqeuenceSize - 2 - i])
        newMovList.append(-movList[sqeuenceSize - 2 - i])

    driveSequ(sqeuenceSize, newOrdList, newMovList)

#Given the co-ords of a point, navigate the robot to it
def goTo(xPos, yPos):
    #find out where the robot is right now
    curX = location.position(X, MM)
    curY = location.position(Y, MM)

    #calculate ho much it need to move
    movX = xPos - curX
    movY = yPos - curY

    #hand off the drive sequence
    driveSequ(2, [X, Y], [movX, movY])


def level1():
    #move to co-ords
    goTo(-500, 700)
    #output the number it stops on
    brain.print("Bot stops on the number 83\n")

#Util function to calculate the number that will be on a grid sqare based on it's co-ordinates
def getGridNum(xPos, yPos):
    #convert the raw co-ords to an internal grid co-ord system
    gridX = ((xPos + 900) / 200) + 1
    gridY = ((yPos + 900) / 200) + 1

    #use the x and y positions of the grid sqares to calculate the number that apears on the square
    if gridX == 10:
        num = gridX * gridY
    else:
        num = ((gridY - 1) * 10) + gridX

    return num

#Part of the core logic for the level 2 solve
def level2Logic(coords):

    #estimate the grid number
    grid = getGridNum(coords[0], coords[1])

    #display it to the consol
    brain.print("Estimated stop on number " + str(grid) + " for the point (" + str(coords[0]) + ", " + str(coords[1]) + "\n")

    #now move the desired co-ords
    goTo(coords[0], coords[1])

def level2():
    #go through the 4 desired locations
    level2Logic([-300, -900])

    level2Logic([700, 700])

    level2Logic([-100, 900])

    level2Logic([500, -300] )

#Another until method that takes a single number and computed the raw co-ords of the square it appears on
def getCoords(gridNum):
    #exeption for multiples of 10
    if gridNum % 10 == 0:
        coords = [10, gridNum / 10]
    else: #extracts the ones and tens coloumn to get the interal x and y to then be converted to the raw co-ords
        coordX = gridNum % 10
        coordY = ((gridNum - coordX ) / 10) + 1

        coords = [coordX,coordY]

    destX = ((coords[0] - 1) * 200) - 900
    destY = ((coords[1] - 1) * 200) - 900

    dest = [destX, destY]

    return dest

def level3Logic(gridNum):

    gotCoords = getCoords(gridNum)

    #brain.print("(" + str(gotCoords[0]) + ", " + str(gotCoords[1]) + ")")

    goTo(gotCoords[0], gotCoords[1])

    wait(2, SECONDS)

def level3():

    level3Logic(22)
    level3Logic(38)
    level3Logic(64)
    level3Logic(85)

# Add project code in "main"
def main():
    init()

    level2()

# VR threads — Do not delete
vr_thread(main())
