""" +=========================================================================================+
    ||                                      Tic-Tac-Toe                                      ||
    ||                         Name: Rashid Lasker   Date: 05/19/15                          ||
    +=========================================================================================+

    This program plays a game of Tic Tac Toe.
"""
#######################################<BEGINNING OF PROGRAM>#######################################
#----------------------------------------------------------------------------------------------------
def makeDictionary():
    database = dict()
    sequence = [0,1,2,3,4,5,6,7,8,]
    filledBoards = list(permutations(sequence,9))
    for perm in filledBoards:
        for lim in range(9):
            board = stringBoard(perm, lim)
            if(not(isThreeInARow(board))):
                database[board] = 0
    print(len(database))
    return database
#----------------------------------------------------------------------------------------------------
def stringBoard(perm, limit):
    newBoard = '---------'
    for n in range (limit):
        if n%2 == 0:
            newBoard = insertX(newBoard, perm.index(n))
        else:
            newBoard = insertO(newBoard, perm.index(n))
    return newBoard
#----------------------------------------------------------------------------------------------------
def insertX(board, num):
    retBoard = board[:num] + 'X' + board[num+1:]
    return retBoard
#----------------------------------------------------------------------------------------------------
def insertO(board, num):
    retBoard = board[:num] + 'O' + board[num+1:]
    return retBoard
#----------------------------------------------------------------------------------------------------
def isThreeInARow(board):
    #0 1 2
    #3 4 5
    #6 7 8
    if board[0] == board[3] == board[6] and not(board[0] == '-'):
        return True
    if board[1] == board[4] == board[7] and not(board[1] == '-'):
        return True
    if board[2] == board[5] == board[8] and not(board[2] == '-'):
        return True
    if board[0] == board[1] == board[2] and not(board[0] == '-'):
        return True
    if board[3] == board[4] == board[5] and not(board[3] == '-'):
        return True
    if board[6] == board[7] == board[8] and not(board[6] == '-'):
        return True
    if board[0] == board[4] == board[8] and not(board[0] == '-'):
        return True
    if board[2] == board[4] == board[6] and not(board[2] == '-'):
        return True
    return False
#-----------------------------------------------<MAIN>-----------------------------------------------
def main():
    database = makeDictionary()


#===============================<GLOBAL CONSTANTS and GLOBAL IMPORTS=================================
from random import random, randint, choice; from math import sqrt; from copy import deepcopy;
from itertools import permutations
from time import clock; START_TIME = clock(); main(); print('\n      +===<RUN TIME>===+');
print('      |  %5.2f'%(clock()-START_TIME), 'seconds |'); print('      +================+')
##########################################<END OF PROGRAM>###########################################