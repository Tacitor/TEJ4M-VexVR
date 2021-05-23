# ------------------------------------------
# 
# 	Project:      Castle Color Match Challenge
#	Author:       Lukas Krampitz
#	Created:      05 May 2021
#	Description:  Have the VEXcode VR robot move and sort coloured discs around the castle court yard
# ------------------------------------------

# Library imports
from vexcode import *

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

#given a path to a disc the robot will drive there, pick it up, and return to the home base
def pickup(ordList, movList):
    driveSequ(len(ordList), ordList, movList)
    magnet.energize(BOOST)
    driveSequRev(len(ordList), ordList, movList)

#given a path to a drop off location the robot will drive there, deposit the magnet, and return to the home base
def dropoff(ordList, movList):
    driveSequ(len(ordList), ordList, movList)
    magnet.energize(DROP)
    driveSequRev(len(ordList), ordList, movList)


def level1():
    #get blue
    pickup([Y, X], [3.5, -1.75])
    dropoff([X], [-4])

    #get red
    pickup([Y, X], [4.5, -2.75])
    dropoff([X], [0.25])

    #get greed
    pickup([Y, X], [3.5, 1.75])
    dropoff([X], [4])    

def level2():

    #get green
    pickup([Y, X], [3.5, 1.75])
    dropoff([X], [4])    
    #get green
    pickup([Y, X], [3.5, 2.75])
    dropoff([X], [4]) 
    #get green
    pickup([Y, X, Y], [4.5, -2.5, 2])
    dropoff([X], [4])
    #get green
    pickup([Y, X, Y], [4.5, -1.5, 2])
    dropoff([X], [4])

    #get blue
    pickup([Y, X, Y], [4.5, 2.5, 1])
    dropoff([X], [-4])
    #get blue
    pickup([Y, X], [3.5, -1.75])
    dropoff([X], [-4])
    #get blue
    pickup([Y, X], [3.5, -2.75])
    dropoff([X], [-4])
    #get blue
    pickup([Y, X], [4.5, 2.75])
    dropoff([X], [-4])

    #get red
    pickup([Y, X], [4.5, -2.75])
    dropoff([Y], [-0.75])
    #get red
    pickup([Y, X, Y], [4.5, -2.5, 1])
    dropoff([Y], [-0.75])
    #get red
    pickup([Y, X, Y], [4.5, 2.5, 2])
    dropoff([Y], [-0.75])
    #get red
    pickup([Y, X, Y], [4.5, 1.5, 2])
    dropoff([Y], [-0.75])

def level3():
    #get green
    pickup([Y, X], [3.5, 1.75])
    dropoff([X], [4])    
    #get green
    pickup([Y, X], [3.5, 2.75])
    dropoff([X], [4]) 
    #get green
    pickup([Y, X, Y], [4.5, -2.5, 2])
    dropoff([X], [4])

    #get blue
    pickup([Y, X, Y], [4.5, 2.5, 1])
    dropoff([X], [-4])
    #get blue
    pickup([Y, X], [3.5, -1.75])
    dropoff([X], [-4])
    #get blue
    pickup([Y, X], [3.5, -2.75])
    dropoff([X], [-4])

    #get red
    pickup([Y, X], [4.5, -2.75])
    dropoff([Y], [-0.75])
    #get red
    pickup([Y, X, Y], [4.5, -2.5, 1])
    dropoff([Y], [-0.75])
    #get red
    pickup([Y, X, Y], [4.5, 2.5, 2])
    dropoff([Y], [-0.75])

    #hide green
    pickup([Y, X, Y], [4.5, -1.5, 2])
    dropoff([Y, X, Y, X], [2, -4.5, 6.6, 4])
    #hide blue
    pickup([Y, X], [4.5, 2.75])
    dropoff([Y, X, Y, X], [2, -4.5, 6.6, 4])
    #hide red
    pickup([Y, X, Y], [4.5, 1.5, 2])
    dropoff([Y, X, Y, X], [2, -4.5, 6.6, 4])
    

# Add project code in "main"
def main():
    #set the speed to be faster
    drivetrain.set_drive_velocity(100, PERCENT)
    drivetrain.set_turn_velocity(100, PERCENT)

    level3()

# VR threads — Do not delete
vr_thread(main())
