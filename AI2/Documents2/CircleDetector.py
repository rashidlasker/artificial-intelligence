""" +=========================================================================================+
    ||                                   Circle Detector                                     ||
    ||                         Name: Rashid Lasker   Date: 3/17/15                           ||
    +=========================================================================================+

    This program converts images to gray scale and blurs them.
"""
#######################################<BEGINNING OF PROGRAM>#######################################
#===============================<GLOBAL CONSTANTS and GLOBAL IMPORTS================================
from random import random, randint, choice; from math import sqrt, atan2, tan, cos, sin; from copy import deepcopy;
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
def circleMatrix(width, height, gMatrix, prunedMatrix):
    maxVotes = 0
    maxR = 0
    maxC = 0
    voteMatrix = []
    radiusMatrix = []
    for r in range(height):
        rowV = []
        rowR = []
        for c in range(width):
            rowV.append(0)
            rowR.append([])
        voteMatrix.append(rowV)
        radiusMatrix.append(rowR)
    for r in range(1, height-1):
        for c in range(1, width-1):
            valueR, valueC = gMatrix[r][c]
            theta = atan2(valueR, valueC)
            if prunedMatrix[r][c] ==1:
                for rad in range(25,500):
                    x = int(c + rad*cos(theta))
                    y = int(r - rad*sin(theta))
                    if x > 0 and x < width and y > 0 and y < height:
                        voteMatrix[y][x] = voteMatrix[y][x] + 1
                        radiusMatrix[y][x].append(rad) 
                for rad in range(25,500):
                    x = int(c - rad*cos(theta))
                    y = int(r + rad*sin(theta))
                    if x > 0 and x < width and y > 0 and y < height:
                        voteMatrix[y][x] = voteMatrix[y][x] + 1
                        radiusMatrix[y][x].append(rad) 
    print('Voting Completed')
    for r in range(height):
        for c in range(width):
            if voteMatrix[r][c] > maxVotes:
                maxVotes = voteMatrix[r][c]
                maxR = r
                maxC = c
    circleRadius = int(sum(radiusMatrix[maxR][maxC])/len(radiusMatrix[maxR][maxC]))
    print(circleRadius)
    print(maxR)
    print(maxC)
    return voteMatrix, maxVotes, maxR, maxC, circleRadius
#-----------------------------------------------<MAIN>----------------------------------------------
def main():
    textfile = open('face.ppm').read().split()
    filetype = textfile.pop(0)
    width = int(textfile.pop(0))
    height = int(textfile.pop(0))
    maxRGB = int(textfile.pop(0))

    oldMatrix = createMatrix(width, height, textfile) #returns matrix with each pixel
    newMatrix = createEdgeMatrix(width, height, oldMatrix) #returns matrix with Gx and Gy
    prunedMatrix = pruneEdgeMatrix(width, height, newMatrix) #returns matrix with 1 and 0 signifying edges
    voteMatrix, maxVotes, maxR, maxC, circleRadius = circleMatrix(width, height, newMatrix, prunedMatrix)
    newFile = open('/afs/csl.tjhsst.edu/students/2016/2016rlasker/Documents2/circleface.ppm', 'w')
    #newFile = open('E:/Documents2/circleface.ppm', 'w')
    newFile.write(filetype + '\n')
    newFile.write(str(width) + ' ' + str(height) + '\n')
    newFile.write(str(maxRGB) + '\n')
    for r in range(height):
        for c in range(width):
            if (pow(c-maxC,2) + pow(r-maxR,2) >= pow(circleRadius,2)) and (pow(c-maxC,2) + pow(r-maxR,2) < pow(circleRadius+1,2)):
                newFile.write(str(0) + ' ' + str(255) + ' ' + str(0) + ' ')
            elif prunedMatrix[r][c] == 1:
                newFile.write(str(255) + ' ' + str(0) + ' ' + str(0) + ' ')
            else:
                val = int(((maxVotes - voteMatrix[r][c])/maxVotes)*255)
                newFile.write(str(val) + ' ' + str(val) + ' ' + str(val) + ' ')
    print('File Completed')
#---------------------------------------------------------------------------------------------------
if __name__ == '__main__': main()
##########################################<END OF PROGRAM>##########################################
