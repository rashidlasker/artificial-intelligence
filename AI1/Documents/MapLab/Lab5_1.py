""" +=========================================================================================+
    ||                             Lab5.1: Romania Map Creator                               ||
    ||                         Name: Rashid Lasker   Date: 9/30/14                           ||
    +=========================================================================================+

    This program generates a dictionary of neighbors for all the words in the given text file
    and stores it in a file.
"""
#######################################<BEGINNING OF PROGRAM>#######################################

def generateDictionaryOfNames():
    nodeFileName = '/afs/csl.tjhsst.edu/students/2016/2016rlasker/Documents/MapLab/romFullNames.txt'
    namesDict = dict()
    namesFile = open(nodeFileName, 'r')
    for line in namesFile:
        name = line.strip()
        namesDict[name[0]] = name
    return namesDict
  
def generateDictionaryOfLocations(namesDict):
    nodeFileName = '/afs/csl.tjhsst.edu/students/2016/2016rlasker/Documents/MapLab/romNodes.txt'
    locationDict = dict()
    nodeFile = open(nodeFileName, 'r')
    for line in nodeFile:
        locList = line.strip().split()
        locationDict[namesDict.get(locList[0])] = [locList[1], locList[2]]
    return locationDict

def generateDictionaryOfNeighbors(namesDict):
    edgeFileName = '/afs/csl.tjhsst.edu/students/2016/2016rlasker/Documents/MapLab/romEdges.txt'
    neighborDict = dict()
    edgefile = open(edgeFileName, 'r')
    for line in edgefile:
        (edge1, edge2) = line.strip().split()
        edge1 = namesDict.get(edge1)
        edge2 = namesDict.get(edge2)
        if edge1 in neighborDict:
            neighborDict.get(edge1).append(edge2)
        else:
            neighborDict[edge1] = [edge2]
        if edge2 in neighborDict:
            neighborDict.get(edge2).append(edge1)
        else:
            neighborDict[edge2] = [edge1]
    return neighborDict
  
def saveDictIntoFile(inputDict,name):
    newFileName = '/afs/csl.tjhsst.edu/students/2016/2016rlasker/Documents/MapLab/' + name + '.txt'
    import pickle
    newFile = open(newFileName, 'wb')
    pickle.dump(inputDict, newFile)
    newFile.close()

def main():
    namesDict = generateDictionaryOfNames()
    locationDict = generateDictionaryOfLocations(namesDict)
    saveDictIntoFile(locationDict, 'romNodesDict')
    saveDictIntoFile(generateDictionaryOfNeighbors(namesDict), 'romNeighborsDict')
    

#===============================<GLOBAL CONSTANTS and GLOBAL IMPORTS================================
from random import random, randint; from math import sqrt; from copy import deepcopy;
from time import clock; START_TIME = clock(); main(); print('\n      +===<RUN TIME>===+');
print('      |  %5.2f'%(clock()-START_TIME), 'seconds |'); print('      +================+')
##########################################<END OF PROGRAM>##########################################