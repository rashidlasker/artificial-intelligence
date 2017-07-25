""" +=========================================================================================+
    ||                                     Lab 10: Ghost                                     ||
    ||                         Name: Rashid Lasker   Date: 11/24/14                          ||
    +=========================================================================================+

    This program plays a game of Ghost.
"""
#######################################<BEGINNING OF PROGRAM>#######################################
#-----------------------------------------------<Node>----------------------------------------------
class Node(object):
    def __init__(self, value):
        self.value = value
        self.children = {}
    #-----------------------------------------------------------------------------------------------
    def __repr__(self):
        self.print()
        return ''
    #-----------------------------------------------------------------------------------------------
    def print(self, stng):
        for key in self.children:
            if key != '$':
                self.children[key].print(stng + key)
            else: print(stng)
    #-----------------------------------------------------------------------------------------------
    def display(self):
        if self.value == '$': return
        #print data
        print ('========== NODE ==========')
        print ('--> self.value     =', self.value)
        print ('--> self.children: [', end = '')
        #print values of children
        for key in self.children:
            if key != '$':
                print(key, end = ', ')
        print(']')
        print('----------------------------')
        #recurse
        for char in self.children:
            (self.children[char]).display()
    #-----------------------------------------------------------------------------------------------
    def insert(self, stng):
         if stng == '':
             self.children['$'] = Node ('$')
             return
         if stng[0] not in self.children:
             p = Node(stng[0])
             self.children[stng[0]] = p
             p.insert(stng[1:])
             return
         self.children[stng[0]].insert(stng[1:])
    #-----------------------------------------------------------------------------------------------
    def search(self, stng):
         if stng == '':
             if '$' in self.children:
                 return True
             else: return False
         if stng[0] in self.children:
             return self.children[stng[0]].search(stng[1:])
         else: return False
    #-----------------------------------------------------------------------------------------------
    def randomChild(self):                                                                
         a = choice(list(self.children.keys()))
         return a
    #-----------------------------------------------------------------------------------------------
    def searchForNextLetter(self, stng):                                             #< WORK ON THIS
         if stng == '':
             return self.randomChild()
         if stng[0] in self.children:
             return self.children[stng[0]].searchForNextLetter(stng[1:])
    #-----------------------------------------------------------------------------------------------
    def fragmentInDictionary(self, stng):
         if stng == '':
             return True
         if stng[0] in self.children:
             return self.children[stng[0]].fragmentInDictionary(stng[1:])
         else: return False
#----------------------------------------------------------------------------------------------------
def createTrieFromDictionaryFile():
    root = Node('*')
    file1 = open('ghostDictionary.txt')
    for word in file1:
        root.insert(word.lower().strip())
    file1.close()
    return root
#----------------------------------------------------------------------------------------------------
def printGhostDirections():
    print(' +--------------------------------+')
    print(' | Welcome to the game of Ghost.  |')
    print(' | The human goes first. Enter    |')
    print(' | your letters in the pop-up     |')
    print(' | dialog boxes. Good Luck!       |')
    print(' +--------------------------------+')
#----------------------------------------------------------------------------------------------------
def spellWordFromString(root, stng):
    if root.search(stng):
        return stng
    else:
        return spellWordFromString(root, stng + root.searchForNextLetter(stng))
#----------------------------------------------------------------------------------------------------
def requestAndCheckHumanMove(root, stng):
    stng += input('HUMAN, enter your character.').lower()[0]
    print(' ', stng)
    if root.search(stng):
        print('----------------------------------------')
        print(' HUMAN LOSES because "', stng, '" is a word.', sep = '')
        exit()
        print('----------------Game Over---------------')
    if root.fragmentInDictionary(stng) == False:
        print('----------------------------------------')
        print(' HUMAN LOSES because "', stng, \
              '"\n does not begin any word.', sep = '')
        print(" [The computer's word was ", '"', \
              spellWordFromString(root, stng[0:-1]),'".]', sep = '')
        exit()
    return(stng)
#----------------------------------------------------------------------------------------------------
def requestAndCheckComputerMove(root, stng):                                          #< WORK ON THIS
    stng += root.searchForNextLetter(stng)
    print(' ', stng)
    if root.search(stng):
        print('----------------------------------------')
        print(' COMPUTER LOSES because "', stng, '" is a word.', sep = '')
        exit()
        print('----------------Game Over---------------')
    return(stng)
#-----------------------------------------------<MAIN>-----------------------------------------------
def main():
    root = createTrieFromDictionaryFile()
    printGhostDirections()
    stng = ''
    while True:
        stng = requestAndCheckHumanMove(root, stng)
        stng = requestAndCheckComputerMove(root, stng)

#===============================<GLOBAL CONSTANTS and GLOBAL IMPORTS=================================
from random import random, randint, choice; from math import sqrt; from copy import deepcopy;
from time import clock; START_TIME = clock(); main(); print('\n      +===<RUN TIME>===+');
print('      |  %5.2f'%(clock()-START_TIME), 'seconds |'); print('      +================+')
##########################################<END OF PROGRAM>###########################################