""" +=========================================================================================+
    ||                                   Edge Detection 2                                    ||
    ||                         Name: Rashid Lasker   Date: 2/5/14                            ||
    +=========================================================================================+

    This program converts images to gray scale and blurs them.
"""
#######################################<BEGINNING OF PROGRAM>#######################################
#===============================<GLOBAL CONSTANTS and GLOBAL IMPORTS================================
from math import atan2
from copy import deepcopy
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
def createBlurMatrix(width, height, oldMatrix):
    newMatrix = deepcopy(oldMatrix)
    for r in range(1, height-1):
        for c in range(1, width-1):
            # 1 2 1
            # 2 4 2
            # 1 2 1
            value = oldMatrix[r - 1][c - 1]*1 + oldMatrix[r - 1][c]*2 + oldMatrix[r - 1][c + 1]*1 + oldMatrix[r][c - 1]*2 + oldMatrix[r][c]*4 + oldMatrix[r][c + 1]*2 + oldMatrix[r + 1][c - 1]*1 + oldMatrix[r + 1][c]*2 + oldMatrix[r + 1][c + 1]*1
            newMatrix[r][c] = int(value/16)
    return newMatrix
#---------------------------------------------------------------------------------------------------
def createEdgeMatrix(width, height, oldMatrix):
    newMatrix = deepcopy(oldMatrix)
    for r in range(height):
        for c in range(width):
            if r == 0 or r == height-1 or c == 0 or c == width -1:
                newMatrix[r][c] = [0,0]
                continue
            # -1  0 1
            # -2  0 2
            # -1  0 1
            valueC = abs(oldMatrix[r - 1][c - 1]*-1 + oldMatrix[r - 1][c]*0 + oldMatrix[r - 1][c + 1]*1 + oldMatrix[r][c - 1]*-2 + oldMatrix[r][c]*0 + oldMatrix[r][c + 1]*2 + oldMatrix[r + 1][c - 1]*-1 + oldMatrix[r + 1][c]*0 + oldMatrix[r + 1][c + 1]*1)
            #  1  2  1
            #  0  0  0
            # -1 -2 -1
            valueR = abs(oldMatrix[r - 1][c - 1]*1 + oldMatrix[r - 1][c]*2 + oldMatrix[r - 1][c + 1]*1 + oldMatrix[r][c - 1]*0 + oldMatrix[r][c]*0 + oldMatrix[r][c + 1]*0 + oldMatrix[r + 1][c - 1]*-1 + oldMatrix[r + 1][c]*-2 + oldMatrix[r + 1][c + 1]*-1)
            if valueC + valueR > 100:
                newMatrix[r][c] = [valueR,valueC]
            else:
                newMatrix[r][c] = [0,0]
    return newMatrix
#---------------------------------------------------------------------------------------------------
def pruneEdgeMatrix(width, height, oldMatrix):
    prunedMatrix = deepcopy(oldMatrix)
    for r in range(1, height-1):
        for c in range(1, width-1):
            valueR, valueC = oldMatrix[r][c]
            if valueR == 0 and valueC == 0:
                prunedMatrix[r][c] = 0
                continue
            theta = atan2(valueR, valueC)
            #  0  0  0
            #  1  0  1
            #  0  0  0
            if (theta < 3.14/8 and theta > -3.14/8) or (theta > 7 * 3.14/8) or (theta < 7 * 3.14/8):
                if ((valueR + valueC) > (oldMatrix[r][c+1][0] + oldMatrix[r][c+1][1])) and ((valueR + valueC) > (oldMatrix[r][c-1][0] + oldMatrix[r][c-1][1])):
                    prunedMatrix[r][c] = 1
                else:
                    prunedMatrix[r][c] = 0
            #  0  0  1
            #  0  0  0
            #  1  0  0
            #if (theta < 3*3.14/8 and theta > 3.14/8) or (theta > -7 * 3.14/8 and theta < -5 * 3.14/8):
                #if ((valueR + valueC) > (oldMatrix[r-1][c+1][0] + oldMatrix[r-1][c+1][1])) and ((valueR + valueC) > (oldMatrix[r+1][c-1][0] + oldMatrix[r+1][c-1][1])):
                    #prunedMatrix[r][c] = 1
                #else:
                    #prunedMatrix[r][c] = 0
            #  0  1  0
            #  0  0  0
            #  0  1  0
            if (theta < 5*3.14/8 and theta > 3*3.14/8) or (theta > -5 * 3.14/8 and theta < -3 * 3.14/8):
                if ((valueR + valueC) > (oldMatrix[r+1][c][0] + oldMatrix[r+1][c][1])) and ((valueR + valueC) > (oldMatrix[r-1][c][0] + oldMatrix[r-1][c][1])):
                    prunedMatrix[r][c] = 1
                else:
                    prunedMatrix[r][c] = 0
            #  1  0  0
            #  0  0  0
            #  0  0  1
            #if (theta < (7*3.14/8) and theta > (5*3.14/8)) or (theta > (-3 * 3.14/8) and theta < (-1 * 3.14/8)):
                #if ((valueR + valueC) > (oldMatrix[r+1][c+1][0] + oldMatrix[r+1][c+1][1])) and ((valueR + valueC) > (oldMatrix[r-1][c-1][0] + oldMatrix[r-1][c-1][1])):
                    #prunedMatrix[r][c] = 1
                #else:
                    #prunedMatrix[r][c] = 0
    return prunedMatrix
#-----------------------------------------------<MAIN>----------------------------------------------
def main():
    textfile = open('circle.ppm').read().split()
    filetype = textfile.pop(0)
    width = int(textfile.pop(0))
    height = int(textfile.pop(0))
    maxRGB = int(textfile.pop(0))

    oldMatrix = createMatrix(width, height, textfile)
    blurMatrix = createBlurMatrix(width, height, oldMatrix)
    newMatrix = createEdgeMatrix(width, height, blurMatrix)
    prunedMatrix = pruneEdgeMatrix(width, height, newMatrix)

    newFile = open('/afs/csl.tjhsst.edu/students/2016/2016rlasker/Documents2/thinedgecircle.ppm', 'w')
    #newFile = open('E:/Documents2/grayface.ppm', 'w')
    newFile.write(filetype + '\n')
    newFile.write(str(width) + ' ' + str(height) + '\n')
    newFile.write(str(maxRGB) + '\n')
    for r in range(height):
        for c in range(width):
            if prunedMatrix[r][c] == 1:
                newFile.write(str(255) + ' ' + str(0) + ' ' + str(0) + ' ')
            else:
                newFile.write(str(255) + ' ' + str(255) + ' ' + str(255) + ' ')
#---------------------------------------------------------------------------------------------------
if __name__ == '__main__': main()
##########################################<END OF PROGRAM>##########################################
