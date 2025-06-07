#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimum_removals' function below.
# 
# The function is expected to return an INTEGER.
# The function accepts INTEGER ARRAY nums as parameter.
#

def minimum_removals(nums):
    n = len(nums)
    

    min_val = min(nums)
    max_val = max(nums)
    
    min_idx = nums.index(min_val)
    max_idx = nums.index(max_val)
    

    a, b = min_idx, max_idx
    if a > b:
        a, b = b, a
    

    front = b + 1                
    back = n - a                 
    mix = (a + 1) + (n - b)      
    
    return min(front, back, mix)

if __name__ == '__main__':
    nums_count = int(input().strip())

    nums = []

    for _ in range(nums_count):
        nums_item = int(input().strip())
        nums.append(nums_item)

    result = minimum_removals(nums)

    print(str(result))
# This code defines a function to calculate the minimum number of removals required to ensure that the minimum and maximum elements of an array are not adjacent.