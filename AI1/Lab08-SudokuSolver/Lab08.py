""" +=========================================================================================+
    ||                                     Lab 8: Sudoku                                     ||
    ||                         Name: Rashid Lasker   Date: 11/4/14                          ||
    +=========================================================================================+

    This program solves sudoku problems
"""
#######################################<BEGINNING OF PROGRAM>#######################################
#----------------------------------------------<GLOBAL>---------------------------------------------
MAX = 9
#-----------------------------------------------<CELL>----------------------------------------------
class Cell(object):
    matrix = None
    def __init__(self, val, r, c, matrix):
        if val != 0:
            self.value = {val,}
        else:
            self.value = {1,2,3,4,5,6,7,8,9,}
        self.num = val
        self.row = r
        self.col = c
        self.block = self.blockNumber(r,c)
        Cell.matrix = matrix
    def blockNumber(self, row, col):
        if     (self.row < 3) and     (self.col < 3): return 0
        if     (self.row < 3) and (2 < self.col < 6): return 1
        if     (self.row < 3) and (5 < self.col)    : return 2
        if (2 < self.row < 6) and     (self.col < 3): return 3
        if (2 < self.row < 6) and (2 < self.col < 6): return 4
        if (2 < self.row < 6) and (5 < self.col)    : return 5
        if (5 < self.row)     and     (self.col < 3): return 6
        if (5 < self.row)     and (2 < self.col < 6): return 7
        if (5 < self.row)     and (5 < self.col)    : return 8
#---------------------------------------------------------------------------------------------------
def createTheSudokuBoard():
##    M = [ [4,8,1,5,0,9,6,7,0,],
##          [3,0,0,8,1,6,0,0,2,],
##          [5,0,0,7,0,3,0,0,8,],
##          [2,0,0,0,0,0,0,0,9,],
##          [9,0,0,0,0,0,0,0,1,],
##          [8,0,0,0,0,0,0,0,4,],
##          [0,3,9,2,7,5,4,8,0,],
##          [6,0,0,0,0,0,9,2,7,],
##          [7,0,0,0,0,0,3,1,0,],]

##    M = [ [0,3,2,0,0,0,0,0,0,],
##          [6,8,0,9,0,0,0,0,5,],
##          [0,1,0,0,0,4,0,7,0],
##          [1,0,0,0,0,9,7,3,0,],
##          [0,7,9,6,0,3,4,8,0,],
##          [0,4,6,7,0,0,0,0,1,],
##          [0,9,0,5,0,0,0,2,0,],
##          [8,0,0,0,0,1,0,9,7,],
##          [0,0,0,0,0,0,6,1,0,],]

##    M = [ [6,0,0,0,4,8,0,0,2,],
##          [8,0,0,5,2,0,0,4,0,],
##          [0,0,0,0,0,7,0,0,0,],
##          [5,0,0,4,0,3,0,2,0,],
##          [0,0,1,0,0,0,9,0,0,],
##          [0,2,0,9,0,5,0,0,8,],
##          [0,0,0,7,0,0,0,0,0,],
##          [0,1,0,0,9,2,0,0,5,],
##          [2,0,0,8,6,0,0,0,3,],]

    M = [ [8,0,0,0,0,0,0,0,0,],
          [0,0,3,6,0,0,0,0,0,],
          [0,7,0,0,9,0,2,0,0,],
          [0,5,0,0,0,7,0,0,0,],
          [0,0,0,0,4,5,7,0,0,],
          [0,0,0,1,0,0,0,3,0,],
          [0,0,1,0,0,0,0,6,8,],
          [0,0,8,5,0,0,0,1,0,],
          [0,9,0,0,0,0,4,0,0,],]

    matrix = []
    for r in range(MAX):
        row = []
        for c in range(MAX):
            row.append(Cell(M[r][c], r, c, matrix))
        matrix.append(row)
    return matrix
#---------------------------------------------------------------------------------------------------
def recursivelySolveTheSudoku(matrix):
    matrix = makeAllPossibleSimpleChangesToMatrix(matrix)
    if badMatrix(matrix) or solutionIsCorrect(matrix):
        return matrix
    oldMatrix = deepcopy(matrix)
    r, c = coordinatesOfCellWithSmallestValueSet(matrix)
    for guess in matrix[r][c].value:
        matrix[r][c].value = {guess,}
        matrix = recursivelySolveTheSudoku(matrix)
        if solutionIsCorrect(matrix):
            return matrix
        matrix = restoreValues(matrix, oldMatrix)
    return matrix
#---------------------------------------------------------------------------------------------------
def makeAllPossibleSimpleChangesToMatrix(matrix): #<- Work on this
    matrix, changed = makeAllPossibleSimpleChangesWithTrickOne(matrix)
    while changed:
        matrix, changed = makeAllPossibleSimpleChangesWithTrickOne(matrix)
    matrix, changedTwo = makeAllPossibleSimpleChangesWithTrickTwo(matrix)
    if changedTwo:
        matrix = makeAllPossibleSimpleChangesToMatrix(matrix)
    return matrix
#---------------------------------------------------------------------------------------------------
def makeAllPossibleSimpleChangesWithTrickOne(matrix):
    rows = [set(),set(),set(), set(),set(),set(), set(),set(),set(),]
    cols = [set(),set(),set(), set(),set(),set(), set(),set(),set(),]
    block = [set(),set(),set(), set(),set(),set(), set(),set(),set(),]
    isChanged = False
    for r in range(MAX):
        for c in range(MAX):
            if matrix[r][c].num != 0:
                rows[r].add(matrix[r][c].num)
                cols[c].add(matrix[r][c].num)
                numOfBlock = matrix[r][c].block
                block[numOfBlock].add(matrix[r][c].num)
    for r in range(MAX):
        for c in range(MAX):
            if matrix[r][c].num == 0:
                matrix[r][c].value = matrix[r][c].value - rows[r]
                matrix[r][c].value = matrix[r][c].value - cols[c]
                numOfBlock = matrix[r][c].block
                matrix[r][c].value = matrix[r][c].value - block[numOfBlock]
    for r in range(MAX):
        for c in range(MAX):
            if matrix[r][c].num == 0:
                if len(matrix[r][c].value) == 1:
                    elem = matrix[r][c].value.pop()
                    matrix[r][c].value.add(elem)
                    matrix[r][c].num = elem
                    isChanged = True
    return matrix, isChanged
#---------------------------------------------------------------------------------------------------
def makeAllPossibleSimpleChangesWithTrickTwo(matrix): # <------------ work on this
    rows = [[],[],[], [],[],[], [],[],[],]
    cols = [[],[],[], [],[],[], [],[],[],]
    block = [[],[],[], [],[],[], [],[],[],]
    isChanged = False
    for r in range(MAX):
        for c in range(MAX):
            rows[r].append(matrix[r][c].value)
            cols[c].append(matrix[r][c].value)
            numOfBlock = matrix[r][c].block
            block[numOfBlock].append(matrix[r][c].value)
    for r in range(MAX):
        for n in range(1, MAX+1):
            rCount = 0
            newR = -1
            newC = -1
            for c in range(MAX):
                if n in rows[r][c]:
                    rCount += 1
                    newR = r
                    newC = c
            if rCount == 1:
                matrix[newR][newC].value = {n}
    for c in range(MAX):
        for n in range(1, MAX+1):
            cCount = 0
            newR = -1
            newC = -1
            for r in range(MAX):
                if n in cols[c][r]:
                    cCount += 1
                    newR = r
                    newC = c
            if cCount == 1:
                matrix[newR][newC].value = {n}
    for b in range(MAX):
        for n in range(1, MAX+1):
            bCount = 0
            newR = -1
            newC = -1
            for r in range(MAX):
                for c in range(MAX):
                    if n in matrix[r][c].value and matrix[r][c].block == b:
                        bCount += 1
                        newR = r
                        newC = c
            if bCount == 1:
                matrix[newR][newC].value = {n}
    for r in range(MAX):
        for c in range(MAX):
            if matrix[r][c].num == 0:
                if len(matrix[r][c].value) == 1:
                    elem = matrix[r][c].value.pop()
                    matrix[r][c].value.add(elem)
                    matrix[r][c].num = elem
                    isChanged = True
    return matrix, isChanged
#---------------------------------------------------------------------------------------------------
def coordinatesOfCellWithSmallestValueSet(matrix):
    minSoFar = 1000
    newR = 0
    newC = 0
    for r in range(MAX):
        for c in range(MAX):
            if len(matrix[r][c].value) != 1 and len(matrix[r][c].value) < minSoFar:
                newR = r
                newC = c
    return newR, newC
#---------------------------------------------------------------------------------------------------
def restoreValues(matrix, oldMatrix):
    for r in range(MAX):
        for c in range(MAX):
            matrix[r][c].value = oldMatrix[r][c].value
            matrix[r][c].num = oldMatrix[r][c].num
    return matrix
#---------------------------------------------------------------------------------------------------
def badMatrix(matrix):
    for r in range(MAX):
        for c in range(MAX):
            if matrix[r][c].value == set():
                return True
    return False
#---------------------------------------------------------------------------------------------------
def solutionIsCorrect(matrix):
    rows = [[],[],[], [],[],[], [],[],[],]
    cols = [[],[],[], [],[],[], [],[],[],]
    for r in range(MAX):
        for c in range(MAX):
            rows[r].append(matrix[r][c].value)
            cols[c].append(matrix[r][c].value)

    block = [[],[],[], [],[],[], [],[],[],]

    block[0] = [matrix[0][0].value, matrix[0][1].value, matrix[0][2].value,
                matrix[1][0].value, matrix[1][1].value, matrix[1][2].value,
                matrix[2][0].value, matrix[2][1].value, matrix[2][2].value,]

    block[1] = [matrix[0][3].value, matrix[0][4].value, matrix[0][5].value,
                matrix[1][3].value, matrix[1][4].value, matrix[1][5].value,
                matrix[2][3].value, matrix[2][4].value, matrix[2][5].value,]

    block[2] = [matrix[0][6].value, matrix[0][7].value, matrix[0][8].value,
                matrix[1][6].value, matrix[1][7].value, matrix[1][8].value,
                matrix[2][6].value, matrix[2][7].value, matrix[2][8].value,]

    block[3] = [matrix[3][0].value, matrix[3][1].value, matrix[3][2].value,
                matrix[4][0].value, matrix[4][1].value, matrix[4][2].value,
                matrix[5][0].value, matrix[5][1].value, matrix[5][2].value,]

    block[4] = [matrix[3][3].value, matrix[3][4].value, matrix[3][5].value,
                matrix[4][3].value, matrix[4][4].value, matrix[4][5].value,
                matrix[5][3].value, matrix[5][4].value, matrix[5][5].value,]

    block[5] = [matrix[3][6].value, matrix[3][7].value, matrix[3][8].value,
                matrix[4][6].value, matrix[4][7].value, matrix[4][8].value,
                matrix[5][6].value, matrix[5][7].value, matrix[5][8].value,]

    block[6] = [matrix[6][0].value, matrix[6][1].value, matrix[6][2].value,
                matrix[7][0].value, matrix[7][1].value, matrix[7][2].value,
                matrix[8][0].value, matrix[8][1].value, matrix[8][2].value,]

    block[7] = [matrix[6][3].value, matrix[6][4].value, matrix[6][5].value,
                matrix[7][3].value, matrix[7][4].value, matrix[7][5].value,
                matrix[8][3].value, matrix[8][4].value, matrix[8][5].value,]

    block[8] = [matrix[6][6].value, matrix[6][7].value, matrix[6][8].value,
                matrix[7][6].value, matrix[7][7].value, matrix[7][8].value,
                matrix[8][6].value, matrix[8][7].value, matrix[8][8].value,]
    for r in rows:
        for n in range(1, MAX+1):
            if {n} not in r:
                return False
    for c in cols:
        for n in range(1, MAX+1):
            if {n} not in c:
                return False
    for b in block:
        for n in range(1, MAX+1):
            if {n} not in b:
                return False
    return True
#---------------------------------------------------------------------------------------------------
def displayTheSudokuBoard(matrix):
    for r in range(MAX):
        for c in range(MAX):
            print(matrix[r][c].value ,' ', end ="")
        print()
def printVerification(matrix):
    if solutionIsCorrect(matrix):
        print('Solution is Correct!')
    else:
        print('Something went wrong...')
#-----------------------------------------------<MAIN>----------------------------------------------
def main():
    matrix = createTheSudokuBoard()
    matrix = recursivelySolveTheSudoku(matrix)
    displayTheSudokuBoard(matrix)
    printVerification(matrix)

#===============================<GLOBAL CONSTANTS and GLOBAL IMPORTS================================
from random import random, randint; from math import sqrt; from copy import deepcopy;
from time import clock; START_TIME = clock(); main(); print('\n      +===<RUN TIME>===+');
print('      |  %5.2f'%(clock()-START_TIME), 'seconds |'); print('      +================+')
##########################################<END OF PROGRAM>##########################################
