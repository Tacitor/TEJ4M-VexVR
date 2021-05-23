# ------------------------------------------
# 
# 	Project:      Basketball Drills Challenge
#	Author:       Lukas Krampitz
#	Created:      05 May 2021
#	Description:  Have the VEXcode VR robot preform a set of bascketball drills to train for its big game tomorrow
# 
# ------------------------------------------

# Library imports
from vexcode import *

#Util function to make linar movement simple
def driveGrid(numMove):
    drivetrain.drive_for(FORWARD, 200 * numMove, MM)

def level1():
    for i in [1,2,4]:
        driveGrid(i)
        driveGrid(-i)

def level2():
    for i in [1,2,4]:
        driveGrid(i)
        drivetrain.turn_to_rotation(180, DEGREES);
        driveGrid(i)
        drivetrain.turn_to_rotation(0, DEGREES);

def level3():
    for i in range(1,9):
        driveGrid(i)
        drivetrain.turn_to_rotation(180, DEGREES);
        driveGrid(i)
        drivetrain.turn_to_rotation(0, DEGREES);

# Add project code in "main"
def main():
    #speed up the robot
    drivetrain.set_drive_velocity(100, PERCENT)
    drivetrain.set_turn_velocity(100, PERCENT)

    level3()

# VR threads — Do not delete
vr_thread(main())
