""" +=========================================================================================+
    ||                                     Line Detector                                     ||
    ||                         Name: Rashid Lasker   Date: 3/19/15                           ||
    +=========================================================================================+

    This program converts images to gray scale and blurs them.
"""
#######################################<BEGINNING OF PROGRAM>#######################################
#===============================<GLOBAL CONSTANTS and GLOBAL IMPORTS================================
from random import random, randint, choice; from math import sqrt, atan2, tan, cos, sin, radians; from copy import deepcopy; from queue import PriorityQueue;
#---------------------------------------------------------------------------------------------------
def createMatrix(width, height, textfile):
    matrix = []
    for r in range(height):
        row = []
        for c in range(width):
            red = int(textfile.pop(0))
            green = int(textfile.pop(0))
            blue = int(textfile.pop(0))
            gray = int(0.30 * red + 0.59 * green + 0.11 * blue)
            row.append(gray)
        matrix.append(row)
    return matrix
#---------------------------------------------------------------------------------------------------
def createEdgeMatrix(width, height, oldMatrix): #returns matrix with Gx and Gy
    newMatrix = deepcopy(oldMatrix)
    for r in range(height):
        for c in range(width):
            if r == 0 or r == height-1 or c == 0 or c == width -1:
                newMatrix[r][c] = [0,0]
                continue
            # -1  0 1
            # -2  0 2
            # -1  0 1
            valueC = oldMatrix[r - 1][c - 1]*-1 + oldMatrix[r - 1][c]*0 + oldMatrix[r - 1][c + 1]*1 + oldMatrix[r][c - 1]*-2 + oldMatrix[r][c]*0 + oldMatrix[r][c + 1]*2 + oldMatrix[r + 1][c - 1]*-1 + oldMatrix[r + 1][c]*0 + oldMatrix[r + 1][c + 1]*1
            #  1  2  1
            #  0  0  0
            # -1 -2 -1
            valueR = oldMatrix[r - 1][c - 1]*1 + oldMatrix[r - 1][c]*2 + oldMatrix[r - 1][c + 1]*1 + oldMatrix[r][c - 1]*0 + oldMatrix[r][c]*0 + oldMatrix[r][c + 1]*0 + oldMatrix[r + 1][c - 1]*-1 + oldMatrix[r + 1][c]*-2 + oldMatrix[r + 1][c + 1]*-1
            if abs(valueC) + abs(valueR) > 100:
                newMatrix[r][c] = [valueR,valueC]
            else:
                newMatrix[r][c] = [0,0]
    print('Edges Completed')
    return newMatrix
#---------------------------------------------------------------------------------------------------
def pruneEdgeMatrix(width, height, oldMatrix):
    prunedMatrix = deepcopy(oldMatrix)
    for r in range(height):
        for c in range(width):
            if r == 0 or r == height-1 or c == 0 or c == width -1:
                prunedMatrix[r][c] = 0
                continue
            valueR, valueC = oldMatrix[r][c]
            if valueR == 0 and valueC == 0:
                prunedMatrix[r][c] = 0
                continue
            theta = atan2(valueR, valueC)
            currG = abs(valueR) + abs(valueC)
            #  0  0  0
            #  1  0  1
            #  0  0  0
            if (theta < 3.14/8 and theta > -3.14/8) or (theta > 7 * 3.14/8) or (theta < 7 * 3.14/8):
                if (currG > (abs(oldMatrix[r][c+1][0]) + abs(oldMatrix[r][c+1][1]))) and (currG > (abs(oldMatrix[r][c-1][0]) + abs(oldMatrix[r][c-1][1]))):
                    prunedMatrix[r][c] = 1
                else:
                    prunedMatrix[r][c] = 0
            #  0  0  1
            #  0  0  0
            #  1  0  0
            if (theta < 3*3.14/8 and theta > 3.14/8) or (theta > -7 * 3.14/8 and theta < -5 * 3.14/8):
                if (currG > (abs(oldMatrix[r-1][c+1][0]) + abs(oldMatrix[r-1][c+1][1]))) and (currG > (abs(oldMatrix[r+1][c-1][0]) + abs(oldMatrix[r+1][c-1][1]))):
                    prunedMatrix[r][c] = 1
                else:
                    prunedMatrix[r][c] = 0
            #  0  1  0
            #  0  0  0
            #  0  1  0
            if (theta < 5*3.14/8 and theta > 3*3.14/8) or (theta > -5 * 3.14/8 and theta < -3 * 3.14/8):
                if (currG > (abs(oldMatrix[r+1][c][0]) + abs(oldMatrix[r+1][c][1]))) and (currG > (abs(oldMatrix[r-1][c][0]) + abs(oldMatrix[r-1][c][1]))):
                    prunedMatrix[r][c] = 1
                else:
                    prunedMatrix[r][c] = 0
            #  1  0  0
            #  0  0  0
            #  0  0  1
            if (theta < (7*3.14/8) and theta > (5*3.14/8)) or (theta > (-3 * 3.14/8) and theta < (-1 * 3.14/8)):
                if (currG > (abs(oldMatrix[r+1][c+1][0]) + abs(oldMatrix[r+1][c+1][1]))) and (currG > (abs(oldMatrix[r-1][c-1][0]) + abs(oldMatrix[r-1][c-1][1]))):
                    prunedMatrix[r][c] = 1
                else:
                    prunedMatrix[r][c] = 0
    print('Pruning Completed')
    return prunedMatrix
#---------------------------------------------------------------------------------------------------
def lineMatrix(width, height, gMatrix, prunedMatrix):
    maxVotes = 0
    maxR = 0
    maxC = 0
    voteMatrix = []
    for theta in range(360):
        rowV = []
        for radius in range(height + width):
            rowV.append(0)
        voteMatrix.append(rowV)

    for theta in range(360):
        for r in range(1, height-1):
            for c in range(1, width-1):
                if prunedMatrix[r][c] == 1:
                    radius = int(c*cos(radians(theta)) + r*sin(radians(theta)))
                    if radius < height + width:
                        voteMatrix[theta][radius] = voteMatrix[theta][radius] + 1
    print('Voting Completed')
    for theta in range(360):
        for radius in range(height + width):
            if voteMatrix[theta][radius] > maxVotes:
                maxVotes = voteMatrix[theta][radius]
    return voteMatrix, maxVotes
#-----------------------------------------------<MAIN>----------------------------------------------
def main():
    textfile = open('geoart2.ppm').read().split()
    filetype = textfile.pop(0)
    width = int(textfile.pop(0))
    height = int(textfile.pop(0))
    maxRGB = int(textfile.pop(0))

    oldMatrix = createMatrix(width, height, textfile) #returns matrix with each pixel
    newMatrix = createEdgeMatrix(width, height, oldMatrix) #returns matrix with Gx and Gy
    prunedMatrix = pruneEdgeMatrix(width, height, newMatrix) #returns matrix with 1 and 0 signifying edges
    voteMatrix, maxVotes = lineMatrix(width, height, newMatrix, prunedMatrix)
    
    q = PriorityQueue(360*(height + width))
    for theta in range(360):
        for radius in range(height + width):
            q.put((maxVotes-voteMatrix[theta][radius], theta, radius))

    lineList = []
    for x in range(75):
        addToList = True
        (votes, theta, radius) = q.get()
        for n in range(len(lineList)):
            if abs(theta - lineList[n][1]) < 3 and abs(radius - lineList[n][2]) < 5:
                addToList = False
                break
        if addToList:
            lineList.append((maxVotes-votes, theta, radius))
    
    print(lineList)
    
    isLine = False
    newFile = open('linegeoart2.ppm', 'w')
    #newFile = open('E:/Documents2/circleface.ppm', 'w')
    newFile.write(filetype + '\n')
    newFile.write(str(width) + ' ' + str(height) + '\n')
    newFile.write(str(maxRGB) + '\n')
    for r in range(height):
        for c in range(width):
            isLine=False
            for x in range(len(lineList)):
                (votes, theta, radius) = lineList[x]
                if radius > c*cos(radians(theta)) + r*sin(radians(theta)) -0.5 and radius < c*cos(radians(theta)) + r*sin(radians(theta)) +0.5:
                    newFile.write(str(0) + ' ' + str(255) + ' ' + str(0) + ' ')
                    isLine = True
                    break
            if not isLine:
                if prunedMatrix[r][c] == 1:
                    newFile.write(str(255) + ' ' + str(0) + ' ' + str(0) + ' ')
                else:
                    newFile.write(str(255) + ' ' + str(255) + ' ' + str(255) + ' ')
    print('File Completed')
#---------------------------------------------------------------------------------------------------
if __name__ == '__main__': main()
##########################################<END OF PROGRAM>##########################################
