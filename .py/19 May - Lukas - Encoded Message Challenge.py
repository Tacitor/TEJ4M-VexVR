# ------------------------------------------
# 
# 	Project:      Encoded Message Challenge
#	Author:       Lukas Krampitz    
#	Created:      19 May 2021
#	Description:  Have the robot drive over a series of blue and green lines and read out the encoded message.
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

#Take a List of 1s and 0s of binary and compute the deciamal value
def binaryToDec(array):
    
    output = 0
    currIndex = 0

    #go through all the indexes of the array backwards
    for i in range( (len(array))):

        #invert the value of i. Have this start at the back and end at the front of the List
        currIndex = len(array) - 1 - i

        #brain.print("\n" + str(i) + "   " + str(currIndex))

        #If there is a 1 written there
        if (array[currIndex] == 1):
            #add the result of rasing 2 to the power of i 
            output = output + (pow(2,i))

    return output #this is now the decimal value

#My own fuction for converting to an ascii character
def decToAscii(num):

    global alpha #list of the alphabet all in capital letters
    alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    alphaVal = num

    #check for a lower case number
    if (num > 94):
        alphaVal = alphaVal - 32
    #get the letter (all uppercase for now)
    alphaVal = alphaVal - 64

    #error handeling and lower case correction
    if (num < 65 or num > 122):
        char = "ERROR"
    elif (num > 94):
        char = alpha[alphaVal - 1].lower()
    else:
        char = alpha[alphaVal - 1]

    return char

def level1():

    data = [0]*8

    #go through the 8 tiles and read the value
    for i in range(8):
        driveGrid(1)

        #red the floor value
        if (down_eye.detect(GREEN)):
            data[7 - i] = 1

        wait(5, MSEC)

    brain.print(str(data))

def level2():

    data = [0]*8

    #go through the 8 tiles and read the value
    for i in range(8):
        driveGrid(1)

        #red the floor value
        if (down_eye.detect(GREEN)):
            data[7 - i] = 1

        wait(5, MSEC)

    brain.print("\nBinary: " + str(data))
    brain.print("\nDecimal: " + str(binaryToDec(data)))
    brain.print("\nASCII: " + str(decToAscii(binaryToDec(data))))

def level3():

    finalOutput = ""

    dist = 8
    numColumn = 5

    #go through all 5 columns
    for j in range(numColumn):

        data = [0]*dist

        #go through the 8 tiles and read the value
        for i in range(dist):
            driveGrid(1)

            #read the floor value
            if (down_eye.detect(GREEN)):
                data[dist - 1 - i] = 1

            wait(5, MSEC)
            drivetrain.set_rotation(0, DEGREES)

        brain.print("\nBinary: " + str(data))
        brain.print("\nDecimal: " + str(binaryToDec(data)))

        ascii = str(decToAscii(binaryToDec(data)))

        brain.print("\nASCII: " + str(ascii))
        #only add it if it's not an error character
        if (not ascii == "ERROR"):
            finalOutput = finalOutput + ascii

        driveGrid(-dist)

        #only move it tot he next coloum if this isn't the last one
        if (not j == (numColumn - 1)):
            drivetrain.turn_to_heading(90, DEGREES)
            driveGrid(2)
            drivetrain.turn_to_heading(0, DEGREES)

    brain.print("\nMessage: " + str(finalOutput))

def level4():

    #test library
    n = int('01010100011001010111001101110100', 2)
    message = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()

    brain.print("Output: " + str(message))

# Add project code in "main"
def main():
    init()

    level4()

# VR threads — Do not delete
vr_thread(main())
