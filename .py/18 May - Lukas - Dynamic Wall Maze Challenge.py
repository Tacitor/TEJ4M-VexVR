# ------------------------------------------
# 
# 	Project:      Dynamic Wall Maze Challenge
#	Author:       Lukas Krampitz    
#	Created:      18 May 2021
#	Description:  Have the robot drive around a maze to find it's exit
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
    drivetrain.drive_for(FORWARD, 250 * numMove, MM)

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

#get the robot's current position in the form of an X&Y pair in a List
def getPos():

    curCoords = [location.position(X, MM), location.position(Y, MM)]

    return curCoords

#the logic for one single maze square movment
#a maze square is the single square unit that the maze is comprised of
#a maze square appears to be about 250 mm
def mazeSquare():

    #save the direction the bot is facing
    curAngle = drivetrain.heading(DEGREES)

    #check the front for a wall
    frontWall = front_eye.detect(RED)
    
    #check the right wall
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    sideWall = front_eye.detect(RED)

    #only drive forward if there is a wall to the side and none to the front
    if (sideWall and not frontWall):
        #return the bot to the "forward heading"
        drivetrain.turn_to_heading(curAngle, DEGREES)
        driveGrid(1)
    elif (not sideWall): #go to the right if the right wall ends with a turn\
        #the bot just checked the right wall so there is no need to rotate
        #"straight ahead" is already right from the curAngle forward position
        driveGrid(1)
    elif (sideWall and frontWall): #if a left turn is needed

        #first check if this is a dead end and the bot needs to turn around
        drivetrain.turn_for(LEFT, 180, DEGREES)
        leftWall = front_eye.detect(RED)

        if (leftWall):
            #if it is a dead end and there IS a wall to the left then the robot needs to make an extra 90 degree turn to leave
            drivetrain.turn_for(LEFT, 90, DEGREES)
        driveGrid(1)

def level3():

    #draw a trail to see where the robot has been
    pen.move(DOWN)

    #keep checking for the ending red checkered floor
    while not down_eye.detect(RED):
        #as long as the robot is not on the ending keep repeating the modual maze check
        mazeSquare()
        wait(10, MSEC)

#this fucntion is used to detect and remove back tracking
#Used in removing the exploration of dead ends and anything that does not lead directly to the exit of a maze
def removeBackTrack(aList):   #'aList' should be a 2D array. len(aList) can be any length but len(aList[x]) can only have a length of 2

    removeItem = True #Does the fuction still need to remove items?

    while removeItem:

        removeStart = -1 #index the removal starts at
        removeEnd = -1 #index the removal ends at
        removeItem = False #nothing has been found to remove yet so (re-)set to false

        #go through the List
        for i in range(len(aList)): #pick an index
            for j in range(len(aList)): #compare it to all other indexes

                #ignore the exact same one
                if (not i == j):
                    #get the x any y positions for that position
                    xPosI = aList[i][0]
                    yPosI = aList[i][1]

                    xPosJ = aList[j][0]
                    yPosJ = aList[j][1]

                    #check if they are very nearly the same spot
                    if (abs(xPosI - xPosJ) < 100 and abs(yPosI - yPosJ) < 100):
                        
                        #make note of the part that needs to be removed
                        removeItem = True
                        removeStart = i
                        removeEnd = j

        #check if items need to be removed
        if (removeItem):
            brain.print("\nRem from: " + str(removeStart) + " - " + str(removeEnd))
            #remove all the elements that are inbetween the duplicates
            for num in range(abs(removeEnd-removeStart)):
                aList.pop(removeEnd)
        
        wait(1, MSEC)

    return aList

def level4():

    #draw trail
    pen.move(DOWN)

    #get the co-ordinates
    curCoords = getPos()
    #save them to a list of places the robot has been
    posList = [curCoords]

    #now complete the maze using the right wall following method
    while not down_eye.detect(RED):
        #preform the single unit action
        mazeSquare()
        #log the new position of the robot
        curCoords = getPos()
        posList.append(curCoords)
        wait(10, MSEC)

    #take the log of position the robot had and remove sections that contain detours taken by the bot
    brain.print("\nPosList: \n" + str(posList))
    posList = removeBackTrack(posList)
    brain.print("\nPosList: \n" + str(posList))

    #change the colour of the trail the bot leaves behind to make the optimal route more obvious
    pen.set_pen_color(GREEN)

    #now go back to beginning using the shortest path
    for i in range( (len(posList) - 2), -1, -1 ):
        goTo(posList[i][0] + 5, posList[i][1] + 5)    

# Add project code in "main"
def main():
    init()

    level4()

# VR threads — Do not delete
vr_thread(main())
