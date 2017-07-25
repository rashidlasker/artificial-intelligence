""" +=========================================================================================+
    ||                               Lab 12: Automatic Ant                                   ||
    ||                         Name: Rashid Lasker   Date: 1/27/14                           ||
    +=========================================================================================+

    This program delves into complexity theory at, ironically, a very simple level.
"""
#######################################<BEGINNING OF PROGRAM>#######################################
def setUpCanvas(root):
    root.title("THE AUTOMATIC ANT by Rashid Lasker.")
    canvas = Canvas(root,width = root.winfo_screenwidth(), height = root.winfo_screenheight(), bg = 'black')
    canvas.pack(expand = YES, fill = BOTH)
    return canvas
#---------------------------------------------------------------------------------------------------
def placeFrameAroundWindow():
    canvas.create_rectangle(5,5, SCREEN_WIDTH, SCREEN_HEIGHT, width = 1, outline = 'GOLD')
#---------------------------------------------------------------------------------------------------
def displayStatistics(startTime):
    elapsedTime = round(clock()-startTime, 2)
    speedPerThousand = round(1000*elapsedTime/STEPS, 2)
    print('+=======< Automated Ant Statistics>=========+')
    print('| ANT MOVES = ', STEPS, 'steps.                 |')
    print('| RUN TIME  =%6.2f'% elapsedTime,       'seconds.                |')
    print('| SPEED     =%6.2f' % speedPerThousand, 'seconds-per-1000-moves. |')
    print('+===========================================+')
    message = 'PROGRAM DONE. Final image is ' + str(STEPS) + ' ant moves in ' + str(elapsedTime) + ' seconds.'
    root.title(message)
#---------------------------------------------------------------------------------------------------
def displayMatrix(matrix):
    print('---MATRIX:')
    for row in matrix:
        [print (x, ' ', end = '') for x in row]
        print()
    print('   ================================')
#---------------------------------------------------------------------------------------------------
def plot(x,y, kolor):
    canvas.create_rectangle(x,y, x+5, y+5, width = 1, fill = kolor)
#---------------------------------------------------------------------------------------------------
def createPixelWorld():
    ROW = SCREEN_WIDTH + 5
    COL = SCREEN_HEIGHT + 5
    matrix = [[0 for c in range(COL)] for r in range(ROW)]
    placeFrameAroundWindow()
    canvas.create_line(0,0,SCREEN_WIDTH, SCREEN_HEIGHT, width = 1, fill = 'RED')
    ant = [0,ANT_START_COL,ANT_START_ROW]
    return ant, matrix
#---------------------------------------------------------------------------------------------------
def move(ant):   #WORK HERE
    if ant[0] == 0:
        ant[2] -=5
    elif ant[0] == 1:
        ant[1] -=5
    elif ant[0] == 2:
        ant[2] +=5
    elif ant[0] == 3:
        ant[1] +=5

    if ant[1] > SCREEN_HEIGHT:
        ant[1] = 5
    if ant[1] < 5:
        ant[1] = SCREEN_HEIGHT

    if ant[2] > SCREEN_WIDTH:
        ant[2] = 5
    if ant[2] < 5:
        ant[2] = SCREEN_WIDTH
    return ant
#---------------------------------------------------------------------------------------------------
def modifyColors(ant, matrix):
    newColor = matrix[ant[2]][ant[1]]
    if HEADING_RULE[newColor] == 0:
        ant[0] = ant[0] + 1
        if ant[0] == 4:
            ant[0] = 0
    else:
        ant[0] = ant[0] - 1
        if ant[0] == -1:
            ant[0] = 3
    nextColor = (newColor + 1)%4
    matrix[ant[2]][ant[1]] = nextColor
    x = ant[2]
    y = ant[1]
    kolor = COLORS[nextColor]
    plot(x,y,kolor)
#---------------------------------------------------------------------------------------------------
def makeTheAntsJourney(ant, matrix):
    message = 'PROGRAM CURRENTLY RUNNING ' + str(STEPS) + ' ant moves in ' + str(SPEED_INC) + ' increments.'
    print(message)
    root.title(message)
    startTime = clock()
    for n in range(STEPS):
        move(ant)
        modifyColors(ant, matrix)
        if n % SPEED_INC == 0:
            canvas.update()
    canvas.update()
    displayStatistics(startTime)
#===============================<GLOBAL CONSTANTS and GLOBAL IMPORTS================================
from tkinter import Tk, Canvas, YES, BOTH
from time import clock
from random import choice
root = Tk()
canvas = setUpCanvas(root)

SCREEN_WIDTH = root.winfo_screenwidth() //5*5 - 15
SCREEN_HEIGHT = root.winfo_screenheight()//5*5 - 90
ANT_START_ROW = SCREEN_WIDTH //(5*2) * 5
ANT_START_COL = SCREEN_HEIGHT//(5*2) * 5
STEPS = 20000
SPEED_INC = 20
COLORS = ('WHITE', 'RED', 'BLUE', 'YELLOW', 'GREEN', 'CYAN', 'MAGENTA', 'GRAY', 'PINK')
HEADING_RULE = (0,1,1,0)
assert len(HEADING_RULE) < len(COLORS)
NUMBER_OF_COLORS = len(HEADING_RULE)
#-----------------------------------------------<MAIN>----------------------------------------------
def main():
    ant, matrix = createPixelWorld()
    makeTheAntsJourney(ant, matrix)
    root.mainloop()
#---------------------------------------------------------------------------------------------------
if __name__ == '__main__': main()
##########################################<END OF PROGRAM>##########################################