""" +=========================================================================================+
    ||                                  Lab03: Word Ladder                                   ||
    ||                         Name: Rashid Lasker   Date: 9/11/14                           ||
    +=========================================================================================+

    This program generates a word ladder between two words and prints it out.
"""
#######################################<BEGINNING OF PROGRAM>#######################################

def getNeighborDictFromFile():
    #fileName = '/afs/csl.tjhsst.edu/students/2016/2016rlasker/Documents/oneChangeDict.txt'
    fileName = 'E:/Documents/oneChangeDict.txt'
    file1 = open(fileName, 'rb')
    import pickle
    neighborDict = pickle.load(file1)
    file1.close()
    return neighborDict

def getWord(dictionary):
    word = input()
    if word in dictionary:
        return word
    else:
        exit('Word is not in dictionary')

def findWordLadder(initialWord, finalWord, dictionary):
    from collections import deque
    queue = []
    queue.append(initialWord)
    alreadyFoundList = {initialWord:'none'}
    parent = 'none'
    count = 0
    while len(queue) != 0:
        count = count + 1
        queue = deque(queue)
        transporter = queue.popleft()
        parent = transporter
        childrenList = dictionary.get(transporter)
        for x in range(len(childrenList)):
            if childrenList[x] not in alreadyFoundList:
                alreadyFoundList[childrenList[x]] = parent
                queue.append(childrenList[x])
        if finalWord in alreadyFoundList:
            createWordLadder(finalWord,alreadyFoundList)
            break
    print('Pops = ' + str(count))

def createWordLadder(finalWord,alreadyFoundList):
    wordLadder = [finalWord]
    currWord = finalWord
    while alreadyFoundList.get(currWord) != 'none':
        currWord = alreadyFoundList.get(currWord)
        wordLadder.append(currWord)
    wordLadder.reverse()
    print('Answer = ' + str(wordLadder))

def main():
    neighborDict = getNeighborDictFromFile()
    print('Type in the first six-letter word: ')
    firstWord = 'silver' #getWord(neighborDict)
    print('Type in the second six-letter word: ')
    secondWord = 'sliver' #getWord(neighborDict)
    findWordLadder(firstWord, secondWord, neighborDict)


#===============================<GLOBAL CONSTANTS and GLOBAL IMPORTS================================
from random import random, randint; from math import sqrt; from copy import deepcopy;
from time import clock; START_TIME = clock(); main(); print('\n      +===<RUN TIME>===+');
print('      |  %5.2f'%(clock()-START_TIME), 'seconds |'); print('      +================+')
##########################################<END OF PROGRAM>##########################################
