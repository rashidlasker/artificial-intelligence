""" +=========================================================================================+
    ||                              Lab02: Dictionary Creator                                ||
    ||                         Name: Rashid Lasker   Date: 9/9/14                            ||
    +=========================================================================================+

    This program generates a dictionary of neighbors for all the words in the given text file
    and stores it in a file.
"""
#######################################<BEGINNING OF PROGRAM>#######################################
def generateListOfWords():
   fileName = '/afs/csl.tjhsst.edu/students/2016/2016rlasker/Documents/words.txt'
   file = open(fileName, 'r')
   words1 = file.read()
   file.close
   return words1.split()

def generateDictionaryOfNeighbors(inputList):
   neighborDict = dict()
   for b in range(0, len(inputList)):
      yourWord = inputList[b]
      neighbors = []
      for n in range(0, len(inputList)):
         thisWord = inputList[n]
         diffLetters = 0
         for x in range(len(thisWord)):
            if yourWord[x] != thisWord[x]:
               diffLetters += 1
            if diffLetters > 1:
               break
         if diffLetters == 1:
            neighbors.append(thisWord)
      neighborDict[yourWord] = neighbors
   return neighborDict

def saveIntoFile(inputDict):
   newFileName = '/afs/csl.tjhsst.edu/students/2016/2016rlasker/Documents/oneChangeDict.txt'
   import pickle
   newFile = open(newFileName, 'wb')
   pickle.dump(inputDict, newFile)
   newFile.close()

def main():
   listOfWords = generateListOfWords()
   print('Number of Values: ' + str(len(listOfWords)))
   saveIntoFile(generateDictionaryOfNeighbors(listOfWords))

#===============================<GLOBAL CONSTANTS and GLOBAL IMPORTS================================
from random import random, randint; from math import sqrt; from copy import deepcopy;
from time import clock; START_TIME = clock(); main(); print('\n      +===<RUN TIME>===+');
print('      |  %5.2f'%(clock()-START_TIME), 'seconds |'); print('      +================+')
##########################################<END OF PROGRAM>##########################################
