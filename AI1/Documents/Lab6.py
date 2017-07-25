""" +=========================================================================================+
    ||                               Lab 6: SEND MORE MONEY                                  ||
    ||                         Name: Rashid Lasker   Date: 10/9/14                           ||
    +=========================================================================================+

    This program solves the general alphametic problem
"""
#######################################<BEGINNING OF PROGRAM>#######################################

def main():
    puzzle = "SEND + MORE == MONEY"
    puzzle = puzzle.upper()
    numSols = 0
    from re import findall
    words = findall('[A-Z]+', puzzle)
    startLetters = {word[0] for word in words}
    keys = ''.join(startLetters) + ''.join(set(''.join(words))-startLetters)
    print(keys)
    numKeys = len(keys)
    numStartLetters = len(startLetters)
    from itertools import permutations
    for values in permutations('1234567890', numKeys):
        isPossible = True
        for n in range(numStartLetters):  
             if values[n] == '0':
                 isPossible = False
                 break;
        if isPossible:
            table = str.maketrans(keys, ''.join(values))
            equation = puzzle.translate(table)
            if eval(equation):
                print('---', equation)
                numSols = numSols + 1
    if(numSols > 0):
        print('All solutions have been found')
        print('Number of Solutions: ', numSols)
    else:
        print('No solutions exist')


#===============================<GLOBAL CONSTANTS and GLOBAL IMPORTS================================
from random import random, randint; from math import sqrt; from copy import deepcopy;
from time import clock; START_TIME = clock(); main(); print('\n      +===<RUN TIME>===+');
print('      |  %5.2f'%(clock()-START_TIME), 'seconds |'); print('      +================+')
##########################################<END OF PROGRAM>##########################################
