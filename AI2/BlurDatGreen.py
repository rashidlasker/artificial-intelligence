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
            if pow(r-height/2,2) + pow(c-width/2,2) < pow(width/3,2):
                newMatrix[r][c] = -1
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
    
    newFile = open('blurfacegreen.ppm', 'w')
    #newFile = open('E:/Documents2/grayface.ppm', 'w')
    newFile.write(filetype + '\n')
    newFile.write(str(width) + ' ' + str(height) + '\n')
    newFile.write(str(maxRGB) + '\n')
    for r in range(height):
        for c in range(width):
            gray = newMatrix[r][c]
            if gray == -1:
                newFile.write(str(0) + ' ' + str(255) + ' ' + str(0) + ' ')
            else:
                newFile.write(str(gray) + ' ' + str(gray) + ' ' + str(gray) + ' ')
#---------------------------------------------------------------------------------------------------
if __name__ == '__main__': main()
##########################################<END OF PROGRAM>##########################################
