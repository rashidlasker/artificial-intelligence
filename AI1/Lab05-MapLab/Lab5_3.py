""" +=========================================================================================+
    ||                             Lab5.3: Railroad Map Creator                              ||
    ||                         Name: Rashid Lasker   Date: 10/2/14                           ||
    +=========================================================================================+

    This program generates a dictionary of neighbors for all the stations in the given text file
    and stores it in a file.
"""
#######################################<BEGINNING OF PROGRAM>#######################################

def generateDictionaryOfNames():
    #nodeFileName = '/afs/csl.tjhsst.edu/students/2016/2016rlasker/Documents/MapLab/rrNodeCity.txt'
    nodeFileName = 'rrNodeCity.txt'
    namesDict = dict()
    namesFile = open(nodeFileName, 'r')
    for line in namesFile:
        name = line.strip().split()
        if len(name) == 3:
            namesDict[name[1] + ' ' + name[2]] = name[0]
        else:
            namesDict[name[1]] = name[0]
    return namesDict

def generateDictionaryOfLocations():
    #nodeFileName = '/afs/csl.tjhsst.edu/students/2016/2016rlasker/Documents/MapLab/rrNodes.txt'
    nodeFileName = 'rrNodes.txt'
    locationDict = dict()
    nodeFile = open(nodeFileName, 'r')
    for line in nodeFile:
        locList = line.strip().split()
        locationDict[locList[0]] = [locList[1], locList[2]]
    return locationDict

def generateDictionaryOfNeighbors():
    #edgeFileName = '/afs/csl.tjhsst.edu/students/2016/2016rlasker/Documents/MapLab/rrEdges.txt'
    edgeFileName = 'rrEdges.txt'
    neighborDict = dict()
    edgefile = open(edgeFileName, 'r')
    for line in edgefile:
        (edge1, edge2) = line.strip().split()
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
    #newFileName = '/afs/csl.tjhsst.edu/students/2016/2016rlasker/Documents/MapLab/' + name + '.txt'
    newFileName = name + '.txt'
    import pickle
    newFile = open(newFileName, 'wb')
    pickle.dump(inputDict, newFile)
    newFile.close()

def main():
    saveDictIntoFile(generateDictionaryOfNames(), 'rrNamesDict')
    saveDictIntoFile(generateDictionaryOfLocations(), 'rrNodesDict')
    saveDictIntoFile(generateDictionaryOfNeighbors(), 'rrNeighborsDict')


#===============================<GLOBAL CONSTANTS and GLOBAL IMPORTS================================
from random import random, randint; from math import sqrt; from copy import deepcopy;
from time import clock; START_TIME = clock(); main(); print('\n      +===<RUN TIME>===+');
print('      |  %5.2f'%(clock()-START_TIME), 'seconds |'); print('      +================+')
##########################################<END OF PROGRAM>##########################################