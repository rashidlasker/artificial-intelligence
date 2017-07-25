""" +=========================================================================================+
    ||                                  Lab03.5: Word Ladder                                   ||
    ||                         Name: Rashid Lasker   Date: 9/11/14                           ||
    +=========================================================================================+

    This program generates a word ladder between two words and prints it out.
"""
#######################################<BEGINNING OF PROGRAM>#######################################

def getNeighborDictFromFile():
    fileName = '/afs/csl.tjhsst.edu/students/2016/2016rlasker/Documents/oneChangeDict.txt'
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
def findWordLadder(initialWord, finalWord, dictionary):
    queue = []
    queue.append(initialWord)
    alreadyFoundList = {initialWord:'none'}
    parent = 'none'
    popCount = 0
    h = (lambda word: sum ([finalWord[n] != word[n] for n in range (6)]))
    while queue:
        popCount += 1
        currentNode = queue.pop(0)
        parent = currentNode
        childrenList = dictionary.get(currentNode)
        for x in range(len(childrenList)):
            if childrenList[x] not in alreadyFoundList:
                alreadyFoundList[childrenList[x]] = parent
                queue.append(childrenList[x])
        if finalWord in alreadyFoundList:
            createWordLadder(finalWord,alreadyFoundList)
            break
        queue.sort(key = h)
    if finalWord not in alreadyFoundList:
        print('No possible path available')
    print('Pops = ' + str(popCount))
#---------------------------------------------------------------------------------------------------
def createWordLadder(finalWord,alreadyFoundList):
    wordLadder = [finalWord]
    currWord = finalWord
    while alreadyFoundList.get(currWord) != 'none':
        currWord = alreadyFoundList.get(currWord)
        wordLadder.append(currWord)
    wordLadder.reverse()
    print('Answer = ' + str(wordLadder))
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
