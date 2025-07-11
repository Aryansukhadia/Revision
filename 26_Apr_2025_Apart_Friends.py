# Apart Friends
# subject Codingcasino
# Description
# Problem Statement

# Ishaan has N friends. During his summer break, he got some free time and planned to visit his friends. All of his friend's houses are connected with the roads. All the roads connected to Ishaan's friend's house are in the form of a tree. Ishaan wants to determine that for each friend's house, what is the maximum distance to another house?

# Input Format

# The first line contains an integer N, the total number of Ishaan's friends.
# The second line contains an integer (N - 1) - Number of roads.
# The third line contains an integer 2, representing that there will be 2 integers in the next N - 1 lines.
# The next N - 1 lines contain 2 integers A and B - representing a route from A to B.
# Output Format

# Print N integers - representing the maximum distance from the ith person's house.
# Constraints

# 1 ≤ N ≤ 200000
# 1 ≤ A , B ≤ N
# Evaluation Parameters

# Sample Input
# 5
# 4
# 2
# 1 2
# 1 3
# 3 4
# 3 5
# Sample Output
# 2
# 3
# 2
# 3
# 3﻿
# Explanation
# From the first friend's house: 1 -> 3 -> 4 = 2 units

# From the second friend house : 2 -> 1 -> 3 -> 4 = 3 units

# From the third friend's house : 3 -> 1 -> 2 = 2 units

# From the fourth friend house : 4 -> 3 -> 1 -> 2 = 3 units

# From the fifth friend house : 5 -> 3 -> 1 -> 2 = 3 units

# Execution time limit

# show less
# cancelRejected
# Python 3
# Evaluation details

from collections import deque, defaultdict

def bfs(start, graph, n):
    dist = [-1] * (n + 1)
    dist[start] = 0
    q = deque([start])
    while q:
        node = q.popleft()
        for neighbor in graph[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                q.append(neighbor)
    return dist

def ApartFriends(N, Houses):
    graph = defaultdict(list)
    
    # Build the tree
    for a, b in Houses:
        graph[a].append(b)
        graph[b].append(a)

    # Step 1: Find farthest from node 1
    dist1 = bfs(1, graph, N)
    u = dist1.index(max(dist1))

    # Step 2: From u, find farthest node v and record distances
    dist_u = bfs(u, graph, N)
    v = dist_u.index(max(dist_u))

    # Step 3: From v, record distances
    dist_v = bfs(v, graph, N)

    # Step 4: For each node, max of dist_u[i] and dist_v[i]
    result = []
    for i in range(1, N + 1):
        result.append(max(dist_u[i], dist_v[i]))

    return result

# I/O Handling
if __name__ == '__main__':
    N = int(input().strip())
    Houses_rows = int(input().strip())
    Houses_columns = int(input().strip())

    Houses = []
    for _ in range(Houses_rows):
        Houses_item = list(map(int, input().rstrip().split()))
        Houses.append(Houses_item)

    result = ApartFriends(N, Houses)
    print('\n'.join(map(str, result)))
