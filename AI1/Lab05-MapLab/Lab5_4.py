""" +=========================================================================================+
    ||                           Lab 5.4: Railroad Shortest Path                             ||
    ||                         Name: Rashid Lasker   Date: 10/3/14                           ||
    +=========================================================================================+

    This program generates the shortest path between two stations.
"""
#######################################<BEGINNING OF PROGRAM>#######################################

def getDictFromFile(name):
    #fileName = '/afs/csl.tjhsst.edu/students/2016/2016rlasker/Documents/MapLab/' + name + '.txt'
    fileName = name + '.txt'
    file1 = open(fileName, 'rb')
    import pickle
    neighborDict = pickle.load(file1)
    file1.close()
    return neighborDict
#---------------------------------------------------------------------------------------------------
def findDistance(firstStation, secondStation, nodesDict):
    from math import pi , acos , sin , cos
    node1 = nodesDict.get(firstStation)
    node2 = nodesDict.get(secondStation)
    y1  = float(node1[0])
    x1  = float(node1[1])
    y2  = float(node2[0])
    x2  = float(node2[1])

    R   = 3958.76

    y1 *= pi/180.0
    x1 *= pi/180.0
    y2 *= pi/180.0
    x2 *= pi/180.0
    return acos( sin(y1)*sin(y2) + cos(y1)*cos(y2)*cos(x2-x1) ) * R
#---------------------------------------------------------------------------------------------------
def findShortestPath(firstStation, finalStation, namesDict, neighborDict, nodesDict):
    firstStationNumber = namesDict.get(firstStation)
    finalStationNumber = namesDict.get(finalStation)
    queue = [(0 + findDistance(firstStationNumber, finalStationNumber, nodesDict), firstStationNumber,[], 0)]
    CLOSED = dict()
    popCount = 0
    isSolutionFound = False
    finalPath = []
    while queue:
        queue.sort()
        (parentF, parentName, parentPath, parentG) = queue.pop(0)
        popCount += 1
        currentPath = []
        currentPath += parentPath
        currentPath.append(parentName)
        if parentName == finalStationNumber:
            print(currentPath)
            print('Length = ' + str(parentG))
            isSolutionFound = True
            break
        CLOSED[parentName] = parentG
        childrenList = neighborDict.get(parentName)
        for currentChild in childrenList:
            currentG = parentG + findDistance(parentName, currentChild, nodesDict)
            newChild = (currentG + findDistance(currentChild, finalStationNumber, nodesDict), currentChild, currentPath, currentG)
            index = 0
            if currentChild in CLOSED:
                if CLOSED[currentChild] <= currentG:
                    continue
                elif CLOSED[currentChild] > (currentG):
                    del CLOSED[currentChild]
                    queue.append(newChild)
            else:
                isAlreadyInOpen = False
                for n in range(len(queue)):
                    if queue[n][1] == currentChild:
                        isAlreadyInOpen = True
                        index = n
                        break
                if not isAlreadyInOpen:
                    queue.append(newChild)
                elif isAlreadyInOpen:
                    if queue[n][3] > (currentG):
                        queue.remove(queue[n])
                        queue.append(newChild)
    if isSolutionFound:
        print('Pops = ' + str(popCount))
    else:
        print('No Solution')
#-----------------------------------------------<Main>----------------------------------------------
def main():
    namesDict = getDictFromFile('rrNamesDict')
    neighborDict = getDictFromFile('rrNeighborsDict')
    nodesDict = getDictFromFile('rrNodesDict')
    firstStation = 'Washington DC'
    finalStation = 'Quebec City'
    findShortestPath(firstStation, finalStation, namesDict, neighborDict, nodesDict)


#===============================<GLOBAL CONSTANTS and GLOBAL IMPORTS================================
from random import random, randint; from math import sqrt; from copy import deepcopy;
from time import clock; START_TIME = clock(); main(); print('\n      +===<RUN TIME>===+');
print('      |  %5.2f'%(clock()-START_TIME), 'seconds |'); print('      +================+')
##########################################<END OF PROGRAM>##########################################
