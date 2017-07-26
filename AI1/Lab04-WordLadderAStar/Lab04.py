""" +=========================================================================================+
    ||                                    Lab04: A* Search                                   ||
    ||                         Name: Rashid Lasker   Date: 9/18/14                           ||
    +=========================================================================================+

    This program generates a word ladder between two words and prints it out.
"""
#######################################<BEGINNING OF PROGRAM>#######################################

def getNeighborDictFromFile():
    #fileName = '/afs/csl.tjhsst.edu/students/2016/2016rlasker/Documents/oneChangeDict.txt'
    fileName = 'oneChangeDict.txt'
    file1 = open(fileName, 'rb')
    import pickle
    neighborDict = pickle.load(file1)
    file1.close()
    return neighborDict
#---------------------------------------------------------------------------------------------------
def checkWord(word, dictionary):
    if word in dictionary:
        return word
    else:
        exit('Word is not in dictionary')
#---------------------------------------------------------------------------------------------------
def h(word, finalWord):
    return sum([finalWord[n] != word[n] for n in range (6)])
#---------------------------------------------------------------------------------------------------
def findWordLadder(initialWord, finalWord, dictionary):
    queue = [(0 + h(initialWord, finalWord), initialWord,[], 0)]
    CLOSED = dict()
    popCount = 0
    maxQueueLength = 0
    while queue:
        popCount += 1
        parentNode = queue.pop(0)
        parentName = parentNode[1]
        parentPath = parentNode[2]
        parentG = parentNode[3]
        currentPath = []
        currentPath += parentPath
        currentPath.append(parentName)
        currentG = parentG + 1
        if parentName == finalWord:
            print(currentPath)
            print('Length = ' + str(len(currentPath)))
            break
        CLOSED[parentName] = parentG
        childrenList = dictionary.get(parentName)
        step5(queue, CLOSED, finalWord, childrenList, currentG, currentPath)
        if len(queue)> maxQueueLength:
            maxQueueLength = len(queue)
        queue.sort()
    print('Longest queue = ' + str(maxQueueLength))
    print('Pops = ' + str(popCount))
#---------------------------------------------------------------------------------------------------
def step5(queue, CLOSED, finalWord, childrenList, currentG, currentPath):
    for currentChild in childrenList:
        newChild = (currentG + h(currentChild, finalWord), currentChild, currentPath, currentG)
        isAlreadyInOpen = False
        index = 0
        for n in range(len(queue)):
            if queue[n][1] == currentChild:
                isAlreadyInOpen = True
                index = n
                break
        if currentChild in CLOSED:
            if CLOSED[currentChild] <= currentG:
                continue
            elif CLOSED[currentChild] > (currentG):
                del CLOSED[currentChild]
                queue.append(newChild)
        elif not isAlreadyInOpen:
            queue.append(newChild)
        elif isAlreadyInOpen:
            if queue[n][3] > (currentG):
                queue.remove(queue[n])
                queue.append(newChild)
#-----------------------------------------------<Main>----------------------------------------------
def main():
    neighborDict = getNeighborDictFromFile()
    firstWord = 'silver'
    secondWord = 'sliver'
    checkWord(firstWord, neighborDict)
    checkWord(secondWord, neighborDict)
    findWordLadder(firstWord, secondWord, neighborDict)


#===============================<GLOBAL CONSTANTS and GLOBAL IMPORTS================================
from random import random, randint; from math import sqrt; from copy import deepcopy;
from time import clock; START_TIME = clock(); main(); print('\n      +===<RUN TIME>===+');
print('      |  %5.2f'%(clock()-START_TIME), 'seconds |'); print('      +================+')
##########################################<END OF PROGRAM>##########################################
