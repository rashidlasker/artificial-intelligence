""" +=========================================================================================+
    ||                                   Lab 7: Fibonacci                                    ||
    ||                         Name: Rashid Lasker   Date: 10/23/14                          ||
    +=========================================================================================+

    This program does fibonacci numbers
"""
#######################################<BEGINNING OF PROGRAM>#######################################

def fib1(num):
    a = 1
    b = 1
    c = 1
    if num < 3:
        return 1
    for x in range(3, num+1):
        c = a + b
        a = b
        b = c
    return c
#---------------------------------------------------------------------------------------------------
def fib2(num):
    if num < 3: return 1
    return fib2(num-1) + fib2(num-2)
#---------------------------------------------------------------------------------------------------
def fib3(num):
    a = 1
    b = 2
    if num < 3:
        return 1
    for x in range(3, int(num/2)+2):
        a = a+b
        b = a+b
    if(num%2 == 0):
        return a
    else:
        return b
#---------------------------------------------------------------------------------------------------
def fib4(num):
    if num == 8: return 21
    elif num == 7: return 13
    elif num == 6: return 8
    elif num == 5: return 5
    elif num == 4: return 3
    elif num == 3: return 2
    elif num < 3: return 1
    return fib2(num-1) + fib2(num-2)
#---------------------------------------------------------------------------------------------------
def fib5(num):
    return[1,1,2,3,5,8,13,21,34,55,89,144][num-2] + [1,1,2,3,5,8,13,21,34,55,89,144][num-3]
#---------------------------------------------------------------------------------------------------
def fib6(num, dict):
    if num in dict.keys():
        return dict[num]
    else:
        newVal = fib6(num-1, dict) + fib6(num-2, dict)
        dict[num] = newVal
        return newVal
#---------------------------------------------------------------------------------------------------
def fib7(num):
    from math import sqrt
    PHI = (1+sqrt(5))/2
    return round((pow(PHI, num) - pow(-1/PHI, num))/sqrt(5))
#---------------------------------------------------------------------------------------------------
def fib8(num):
    from decimal import Decimal, getcontext
    from math import sqrt
    if num > 70:
        getcontext().prec = 2*num
    phi1 = (1+sqrt(5))/2
    phi2 = -1/phi1
    return round((pow(phi1, num) - pow(phi2, num))/sqrt(5))
#-----------------------------------------------<MAIN>----------------------------------------------
def main():
    n = 100000; start = clock()
    print('1. fib1(',n,')= ', fib1(n))
    print('   time =', round(clock()-start, 1), 'seconds')

##    n = 100; start = clock()
##    print('2. fib2(',n,')= ', fib2(n))
##    print('   time =', round(clock()-start, 1), 'seconds')

    n = 100000; start = clock()
    print('3. fib3(',n,')= ', fib3(n))
    print('   time =', round(clock()-start, 1), 'seconds')

    n = 39; start = clock()
    print('4. fib4(',n,')= ', fib4(n))
    print('   time =', round(clock()-start, 1), 'seconds')

    n = 12; start = clock()
    print('5. fib5(',n,')= ', fib5(n))
    print('   time =', round(clock()-start, 1), 'seconds')

    n = 950; start = clock()
    print('6. fib6(',n,')= ', fib6(n, {1:1, 2:1}))
    print('   time =', round(clock()-start, 1), 'seconds')

    n = 70; start = clock()
    print('7. fib7(',n,')= ', fib7(n))
    print('   time =', round(clock()-start, 1), 'seconds')

    n = 80; start = clock()
    print('8. fib8(',n,')= ', fib8(n))
    print('   time =', round(clock()-start, 1), 'seconds')



#===============================<GLOBAL CONSTANTS and GLOBAL IMPORTS================================
from random import random, randint; from math import sqrt; from copy import deepcopy;
from time import clock; START_TIME = clock(); main(); print('\n      +===<RUN TIME>===+');
print('      |  %5.2f'%(clock()-START_TIME), 'seconds |'); print('      +================+')
##########################################<END OF PROGRAM>##########################################
