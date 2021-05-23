# ------------------------------------------
# 
# 	Project:      Find Your Age Challenge
#	Author:       Lukas Krampitz
#	Created:      07 May 2021
#	Description:  Have the VEXcode VR robot move to grid squares regarding my age
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

#put a small linear pen mark of the ground
def markSquare():
    #lower pen
    pen.move(DOWN)
    #make the mark
    drivetrain.drive_for(FORWARD, 50, MM)
    #return back to initial position
    drivetrain.drive_for(FORWARD, -50, MM)
    #raise the pen again 
    pen.move(UP)

def level1():
    #get the co-ordinates of the destination square
    coords = getCoords(18)
    #hand them off to the movement function
    goTo(coords[0], coords[1])

def level2():

    coords = getCoords(18)

    goTo(coords[0], coords[1])

    coords = getCoords(2035 - 2003)

    goTo(coords[0], coords[1])

def level3():

    coords = getCoords(31)

    goTo(coords[0], coords[1])
    
    pen.set_pen_color(BLUE)
    markSquare() #put a mark on the square

    coords = getCoords(1)

    goTo(coords[0], coords[1])
    pen.set_pen_color(RED)
    markSquare()

    coords = getCoords(3)

    goTo(coords[0], coords[1])
    pen.set_pen_color(GREEN)
    markSquare()

def level4(destNum):

    coords = getCoords(destNum)

    goTo(coords[0], coords[1])


# Add project code in "main"
def main():
    init()

    level4(78)


# VR threads — Do not delete
vr_thread(main())
