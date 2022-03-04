#!/bin/python3

import math
import os
import random
import re
import sys


def sum_hourglass(arr: list, i, j) -> int:
    result = 0 
    result += arr[i-1][j-1]
    result += arr[i-1][j]
    result += arr[i-1][j+1]
    result += arr[i][j]
    result += arr[i+1][j-1]
    result += arr[i+1][j]
    result += arr[i+1][j+1]
    
    return result

if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    maximum_hourglass = -3000
    for i in range(1, len(arr) -1):
        for j in range(1, len(arr[i]) - 1):
            if maximum_hourglass < sum_hourglass(arr, i, j):
                maximum_hourglass = sum_hourglass(arr, i, j)
                
    print(maximum_hourglass)
