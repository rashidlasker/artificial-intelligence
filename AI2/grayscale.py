""" +=========================================================================================+
    ||                                     Grayscalify                                       ||
    ||                         Name: Rashid Lasker   Date: 2/3/14                            ||
    +=========================================================================================+

    This program converts images to gray scale.
"""
#######################################<BEGINNING OF PROGRAM>#######################################
#===============================<GLOBAL CONSTANTS and GLOBAL IMPORTS================================
from math import atan2 
#-----------------------------------------------<MAIN>----------------------------------------------
def main():
    textfile = open('panda.ppm').read().split()
    filetype = textfile.pop(0)
    width = int(textfile.pop(0))
    height = int(textfile.pop(0))
    maxRGB = int(textfile.pop(0))
    
    newFile = open('graypanda.ppm', 'w')
    #newFile = open('E:/Documents2/grayface.ppm', 'w')
    newFile.write(filetype + '\n')
    newFile.write(str(width) + ' ' + str(height) + '\n')
    newFile.write(str(maxRGB) + '\n')
    for x in range(width*height):
        red = int(textfile.pop(0))
        green = int(textfile.pop(0))
        blue = int(textfile.pop(0))
        gray = int(0.30 * red + 0.59 * green + 0.11 * blue)
        newFile.write(str(gray) + ' ' + str(gray) + ' ' + str(gray) + ' ')
#---------------------------------------------------------------------------------------------------
if __name__ == '__main__': main()
##########################################<END OF PROGRAM>##########################################