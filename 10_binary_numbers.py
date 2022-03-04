#!/bin/python3

import math
import os
import random
import re
import sys

def convert_to_binary(n: int) -> list:
    result = []
    if n == 0:
        result.append('0')
    while n != 0:
        result.append(n % 2)
        n = n // 2
    return reversed(result)

def count_ones(arr: list) -> int:
    counter = 0
    max_counter = 0
    for i in arr:
        if i == 1:
            counter += 1

        if counter > max_counter:
            max_counter = counter

        if i == 0:
            counter = 0
        
    return max_counter

if __name__ == '__main__':
    n = int(input().strip())
    binary = convert_to_binary(n)
    print(count_ones(binary))
    