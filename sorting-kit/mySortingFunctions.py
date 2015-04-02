# Name: Sean Donohoe
# Email: sedo8743@colorado.edu
# SUID: 102296078
#

import sys
import random
import time

# --------- Insertion Sort -------------
# Implementation of getPosition
# Helper function for insertionSort
def getPosition(rList, elt):
    # Find the position where element occurs in the list
    #
    for (i,e) in enumerate(rList):
        if (e >= elt):
            return i
    return len(rList)

# Implementation of Insertion Sort 
def insertionSort(lst):
    n = len(lst)
    retList = []
    for i in lst:
        pos = getPosition(retList,i)
        retList.insert(pos,i)    
    return retList

#------ Merge Sort --------------
def mergeSort(lst):
    # TODO: Implement mergesort here
    # You can add additional utility functions to help you out.
    # But the function to do mergesort should be called mergeSort
    if (len(lst) <= 1):
        return lst
    else:
        mid = int((len(lst)) / 2)
        left = mergeSort(lst[0:mid])
        right = mergeSort(lst[mid:len(lst)])
        newL = merge(left, right)
        return newL

def merge(left, right):
    llen = len(left)
    rlen = len(right)
    
    lptr = 0
    rptr = 0
    
    merged = []
    while (lptr < llen and rptr < rlen):
        if (left[lptr] <= right[rptr]):
            merged.append(left[lptr])
            lptr += 1
        else:
            merged.append(right[rptr])
            rptr += 1
    
    for i in range(lptr, llen):
        merged.append(left[i])
    for v in range(rptr, rlen):
        merged.append(right[v])
    return merged
#------ Quick Sort --------------
def quickSort(lst):
    # TODO: Implement quicksort here
    # You may add additional utility functions to help you out.
    # But the function to do quicksort should be called quickSort
    if (len(lst) <= 1):
        return lst
    (q, plst) = randPartition(lst)
    left = quickSort(plst[0:q])
    right = quickSort(plst[q + 1:len(plst)])
    left.append(plst[q])
    return left + right

def randPartition(lst):
    pivotP = random.randint(0, len(lst) - 1)
    lst[len(lst) - 1], lst[pivotP] = lst[pivotP], lst[len(lst) - 1]
    return partition(lst)

def partition(lst):
    i = -1
    pivot = lst[len(lst) - 1]
    for j in range(0, len(lst) - 1):
        if (lst[j] <= pivot):
            i += 1
            lst[j], lst[i] = lst[i], lst[j]
    i += 1
    lst[len(lst) - 1], lst[i] = lst[i], lst[len(lst) - 1]
    return (i, lst)


# ------ Timing Utility Functions ---------

# Function: generateRandomList
# Generate a list of n elements from 0 to n-1
# Shuffle these elements at random

def generateRandomList(n):
   # Generate a random shuffle of n elements
   lst = list(range(0,n))
   random.shuffle(lst)
   return lst


def measureRunningTimeComplexity(sortFunction,lst):
    t0 = time.clock()
    sortFunction(lst)
    t1 = time.clock() # A rather crude way to time the process.
    return (t1 - t0)


# --- TODO

# Write code to extract average/worst-case time complexity



