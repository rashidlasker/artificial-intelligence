""" +=========================================================================================+
    ||                                     Blurrrrrrrr                                       ||
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
#-----------------------------------------------<MAIN>----------------------------------------------
def main():
    textfile = open('face.ppm').read().split()
    filetype = textfile.pop(0)
    width = int(textfile.pop(0))
    height = int(textfile.pop(0))
    maxRGB = int(textfile.pop(0))
    
    oldMatrix = createMatrix(width, height, textfile)
    newMatrix = createBlurMatrix(width, height, oldMatrix)
    
    newFile = open('blurface.ppm', 'w')
    #newFile = open('E:/Documents2/grayface.ppm', 'w')
    newFile.write(filetype + '\n')
    newFile.write(str(width) + ' ' + str(height) + '\n')
    newFile.write(str(maxRGB) + '\n')
    for r in range(height):
        for c in range(width):
            gray = newMatrix[r][c]
            newFile.write(str(gray) + ' ' + str(gray) + ' ' + str(gray) + ' ')
#---------------------------------------------------------------------------------------------------
if __name__ == '__main__': main()
##########################################<END OF PROGRAM>##########################################
