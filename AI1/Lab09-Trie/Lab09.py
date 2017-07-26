""" +=========================================================================================+
    ||                                      Lab 9: Trie                                      ||
    ||                         Name: Rashid Lasker   Date: 11/20/14                          ||
    +=========================================================================================+

    This program builds a trie
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
#-----------------------------------------------<MAIN>-----------------------------------------------
def main():
    root = Node('*')
    root.insert('cat')
    root.insert('catnip')
    root.insert('cats')
    root.insert('catnap')
    root.insert("can't")
    root.insert('cat-x')
    root.insert('dog')
    root.insert('dogs')
    root.insert('dognip')
    root.print('')
    #root.display()
    print('SEARCH', root.search('junk'))

#===============================<GLOBAL CONSTANTS and GLOBAL IMPORTS================================
from random import random, randint; from math import sqrt; from copy import deepcopy;
from time import clock; START_TIME = clock(); main(); print('\n      +===<RUN TIME>===+');
print('      |  %5.2f'%(clock()-START_TIME), 'seconds |'); print('      +================+')
##########################################<END OF PROGRAM>##########################################
