#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
meal_cost = None
#  2. INTEGER tip_percent
tip_percent = None
#  3. INTEGER tax_percent
tax_percent = None
#

def solve(double: meal_cost, int: tip_percent, tax_percent):
    # Write your code here
    result = meal_cost + meal_cost * tip_percent/100 + meal_cost * tax_percent /100
    
    print(round(result))
    

if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)
