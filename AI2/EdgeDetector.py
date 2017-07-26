""" +=========================================================================================+
    ||                                    Edge Detection                                     ||
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
def createEdgeMatrix(width, height, oldMatrix):
    newMatrix = deepcopy(oldMatrix)
    for r in range(1, height-1):
        for c in range(1, width-1):
            # -1  0 1
            # -2  0 2
            # -1  0 1
            valueC = abs(oldMatrix[r - 1][c - 1]*-1 + oldMatrix[r - 1][c]*0 + oldMatrix[r - 1][c + 1]*1 + oldMatrix[r][c - 1]*-2 + oldMatrix[r][c]*0 + oldMatrix[r][c + 1]*2 + oldMatrix[r + 1][c - 1]*-1 + oldMatrix[r + 1][c]*0 + oldMatrix[r + 1][c + 1]*1)
            #  1  2  1
            #  0  0  0
            # -1 -2 -1
            valueR = abs(oldMatrix[r - 1][c - 1]*1 + oldMatrix[r - 1][c]*2 + oldMatrix[r - 1][c + 1]*1 + oldMatrix[r][c - 1]*0 + oldMatrix[r][c]*0 + oldMatrix[r][c + 1]*0 + oldMatrix[r + 1][c - 1]*-1 + oldMatrix[r + 1][c]*-2 + oldMatrix[r + 1][c + 1]*-1)
            if valueC + valueR > 100:
               newMatrix[r][c] = -1
    return newMatrix
#-----------------------------------------------<MAIN>----------------------------------------------
def main():
    textfile = open('circle.ppm').read().split()
    filetype = textfile.pop(0)
    width = int(textfile.pop(0))
    height = int(textfile.pop(0))
    maxRGB = int(textfile.pop(0))
    
    oldMatrix = createMatrix(width, height, textfile)
    newMatrix = createEdgeMatrix(width, height, oldMatrix)
    
    newFile = open('edgecircle.ppm', 'w')
    #newFile = open('E:/Documents2/grayface.ppm', 'w')
    newFile.write(filetype + '\n')
    newFile.write(str(width) + ' ' + str(height) + '\n')
    newFile.write(str(maxRGB) + '\n')
    for r in range(height):
        for c in range(width):
            val = newMatrix[r][c]
            if val == -1:
                newFile.write(str(255) + ' ' + str(0) + ' ' + str(0) + ' ')
            else:
                newFile.write(str(255) + ' ' + str(255) + ' ' + str(255) + ' ')
#---------------------------------------------------------------------------------------------------
if __name__ == '__main__': main()
##########################################<END OF PROGRAM>##########################################
