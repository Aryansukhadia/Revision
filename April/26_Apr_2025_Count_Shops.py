# Count Of Shops
# subject Codingcasino
# Description
# Problem Statement
# There is a Market that has N shops. You are given a 0-indexed array of paths where paths[i] indicate that there is a directed edge from shop i to shop paths[i]

# Assume the following process in the graph:

# You start from any shop 's' and keep visiting other shops through paths until you reach a shop that you have already visited before on this same process.

# Return an array Count where Count[i] indicates the number of different shops that you will visit if you start the process from shop i.

# Note: There are only N-directed edges.

# Input Format

# The First line of input contains an integer N 
# The next N line of the input contains N integers
# Constraints

# 1 <= N <= 105
# 0 <= paths[i] < N
# Output Format

# It will be an array of counts that indicates the number of different shops that you will visit. 
# Sample test case

# Input 1

# 4
# 1
# 2
# 0
# 0
# Output 1

# 3
# 3
# 3
# 4
# Explanation

# N=4

# 1 (indicate that there is a directed edge from shop 0 to shop 1 )

# 2 (indicate that there is a directed edge from shop 1 to shop 2 )

# 0 (indicates that there is a directed edge from shop 2 to shop 0 )

# 0 (indicates that there is a directed edge from shop 3 to shop 0 )



# It is 3 -> 0 -> 1->2 ->0

# If i=0 , Count[i]=3 (0,1,2)

# If i=1 , Count[i]=3 (1,2,0)

# If i=2 , Count[i]=3 (2,0,1)

# If i=3 , Count[i]=4 (3,0,1,2)

# Input 2

# 5
# 1
# 0
# 1
# 2
# 3
# Output 2

# 2
# 2
# 3
# 4
# 5
# Execution time limit
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countVisitedShops' function below.
# 
# The function is expected to return an INTEGER ARRAY.
# The function accepts INTEGER ARRAY paths as parameter.
#

def countVisitedShops(paths):
    visited = set()
    current_position = 0
    visited.add(current_position)

    result = []

    for move in paths:
        current_position += move
        visited.add(current_position)
        result.append(len(visited))  # Count of unique shops visited so far

    return result

if __name__ == '__main__':
    paths_count = int(input().strip())

    paths = []

    for _ in range(paths_count):
        paths_item = int(input().strip())
        paths.append(paths_item)

    result = countVisitedShops(paths)

    print('\n'.join(map(str, result)))


