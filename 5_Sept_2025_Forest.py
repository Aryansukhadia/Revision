# Forest Fire Spread
# subject Codingcasino
# Description
# Problem Statement
# In a vast forest with n checkposts (numbered 0 to n-1), the fire starts at checkpost '0' and reaches checkpost h at time 0.

# Given a 2D array arr[i] = [xi, yi, timei], where two checkposts xi and yi are connected at timei, if either gets fire before or at timei, the other ignites. If a checkpost doesn't catch fire by the time it's connected, the connection is no longer relevant. This implies that if, in the future, either of them catches fire, they cannot use this relation to ignite other one . The fire may simultaneously reach multiple places (checkposts).

# Return a list of checkposts reached by the fire. The result should be in increasing order.

# Note

# If the fire reaches checkpost '2', it does not necessarily mean that the fire has also reached checkpost '1'.
# Input Format
# The First line of input contains an integer n. 
# The Second line of input contains an integer h.
# The third and fourth lines of input contain an integer x (length of arr) and 3 (length of arr[i] ), which indicate the row and column of the 2d array. 
# The next x lines of the input contain three integers.
# Constraints
# 2 <= n <= 105
# 1 <= arr.length <= n
# arr[i].length == 3
# 0 <= xi, yi <= n - 1
# xi != yi
# 1 <= timei <= 105
# 1 <=h <= n - 1
# Output Format
# Return an array that indicates the list of all the checkposts where fire has reached (or burned). 
# Sample test case
# Input
# 6
# 1
# 3
# 3
# 1 2 5
# 2 3 8
# 1 5 10


# Output
# 0
# 1
# 2
# 3
# 5
# Explanation


# According to the problem, the fire started from checkpost 0, and the fire reached checkpost h (here, h is 1) at time 0.

# At time 5, the fire spread from checkpost 1 to checkpost 2.
# At time 8, the fire spread from checkpost 2 to checkpost 3.
# At time 10, the fire spread from checkpost 1 to checkpost 5.​​​​
# Thus, checkposts 0, 1, 2, 3, and 5 are burned (checkposts where fire reached).

# Execution time limit

#!/bin/python3

import heapq
import sys

def findAllCheckposts(n, h, arr):
    from collections import defaultdict

    # Step 1: Build edge list sorted by time
    arr.sort(key=lambda x: x[2])  # Sort by timei

    # Step 2: Burn starts at 0 and h at time 0
    burn_time = [float('inf')] * n
    burn_time[0] = 0
    burn_time[h] = 0

    # Step 3: Use a queue to simulate spreading
    burned = set([0, h])
    pq = [(0, 0), (0, h)]  # (time, node)

    while pq:
        t, node = heapq.heappop(pq)
        new_arr = []
        for xi, yi, timei in arr:
            if timei < t:
                continue  # too late
            if xi == node or yi == node:
                other = yi if xi == node else xi
                if other not in burned and timei >= burn_time[node]:
                    burn_time[other] = timei
                    burned.add(other)
                    heapq.heappush(pq, (timei, other))
            else:
                # Re-add the edge for later consideration
                new_arr.append([xi, yi, timei])
        arr = new_arr

    return sorted(burned)
