
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
# 
# The function is expected to return a STRING.
# The function accepts INTEGER ARRAY a as parameter.
#

def solve(a):
    a.sort()
    for i in range(len(a) - 1):
        if a[i + 1] % a[i] != 0:
            return "No"
    return "Yes"

if __name__ == '__main__':
    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    result = solve(a)

    print(result)
