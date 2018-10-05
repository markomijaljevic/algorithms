#!/bin/python3
import math
import sys

def diagonalDifference(arr): 
    #print(int(math.sqrt(len(arr))),"  ...  " ,math.sqrt(len(arr)))
    if len(arr) < 4 or int(math.sqrt(len(arr))) < math.sqrt(len(arr)) :
        return "Use only square matrix"

    sumOfLeftDiagonal = 0
    sumOfRightDiagonal = 0
    n = int(math.sqrt(len(arr)))

    for i in range(0,n):
        sumOfLeftDiagonal += arr[(n*i)+i] 
        sumOfRightDiagonal += arr[(n*i)+(n-i-1)]       

    #print(sumOfLeftDiagonal, sumOfRightDiagonal)
    return abs(sumOfLeftDiagonal - sumOfRightDiagonal)

if __name__ == '__main__':
    arr=[7,8,9,10,3,2,-2,11,4,-6,-7,8,3,-2,15,2]
    result = diagonalDifference(arr)
    print(result)