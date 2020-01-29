#!/bin/python3

def sort(array: list) -> list:
    stop = False
    inteArray = array.copy()
    inteArray = averageList(internalSort(inteArray))
    while not isSorted(inteArray) and not stop:
        #print(inteArray)
        inteArray = averageList(internalSort(inteArray))
        stop = True

    print(isSorted(inteArray), inteArray)

    return inteArray

def internalSort(unsortedArray: list) -> list:
    sortedArrays = [[]]

    previousElement = -6969696969696969
    currentArray = 0

    for i in unsortedArray:
        if i >= previousElement:
            try:
                sortedArrays[currentArray].append(i)
            except:
                sortedArrays.append([])
                sortedArrays[currentArray].append(i)
            previousElement = i
        else:
            currentArray = currentArray + 1
            previousElement = -6969696969696969
            try:
                sortedArrays[currentArray].append(i)
            except:
                sortedArrays.append([])
                sortedArrays[currentArray].append(i)
            previousElement = i
    print(sortedArrays)
    return sortedArrays

def isSorted(array: list) -> bool:
    previous = -6969696969696969
    verySorted = True
    for i in array:
        if i < previous:
            verySorted = False
        previous = i
    return verySorted

def averageList(array: list) -> list:
    sortArray = []
    sortDict = {}
    for i in array:
        elem = 0 
        average = -6969696969696969
        for a in i:
            if elem == 0:
                average = a
            else:
                average += a
        sortDict[average] = i
        elem += 1
    for i in sorted(sortDict.keys()):
        sortArray += sortDict[i]
    print(sortArray)
    return sortArray

if __name__ == "__main__":
    import numpy as np
    unsortedArray = np.random.randint(0, 50, 50)
    print(unsortedArray)
    sorta = sort(unsortedArray)
    print(sorta)