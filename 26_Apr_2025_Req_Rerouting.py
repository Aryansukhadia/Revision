#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict, deque

#
# Complete the 'reroute_requests' function below.
# 
# The function is expected to return an INTEGER ARRAY.
# The function accepts following parameters:
# 1. INTEGER N
# 2. INTEGER 2D ARRAY connections
# 3. INTEGER 2D ARRAY events
#

def reroute_requests(N, connections, events):
    # Build the network graph (adjacency list)
    graph = defaultdict(list)
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)

    alive = [True] * N  # Track which servers are alive
    result = []

    for event_type, server in events:
        if event_type == 2:
            # Server failure
            alive[server] = False
        elif event_type == 1:
            if alive[server]:
                # Directly route if server is alive
                result.append(server)
            else:
                # BFS to find the smallest-numbered alive server
                visited = [False] * N
                queue = deque([server])
                found = -1

                while queue:
                    current = queue.popleft()
                    if visited[current]:
                        continue
                    visited[current] = True

                    if alive[current]:
                        if found == -1 or current < found:
                            found = current

                    for neighbor in graph[current]:
                        if not visited[neighbor]:
                            queue.append(neighbor)

                result.append(found if found != -1 else -1)

    return result


if __name__ == '__main__':
    N = int(input().strip())

    connections_rows = int(input().strip())
    connections_columns = int(input().strip())

    connections = []
    for _ in range(connections_rows):
        connections_item = list(map(int, input().rstrip().split()))
        connections.append(connections_item)

    events_rows = int(input().strip())
    events_columns = int(input().strip())

    events = []
    for _ in range(events_rows):
        events_item = list(map(int, input().rstrip().split()))
        events.append(events_item)

    result = reroute_requests(N, connections, events)

    print('\n'.join(map(str, result)))
	
# Request Rerouting
# subject Codingcasino
# Description
# Problem Statement
# You are given N servers in a network numbered from 0 to N-1. These servers are interconnected, and the connections between them are represented as pairs of values in an array. Each pair indicates a bidirectional connection between two servers.

# At any given time, some servers might fail. When a server fails, it can no longer directly receive requests. However, it can still be used as an intermediate node to route requests to other servers.

# When a request is sent to a server that has failed, it needs to be rerouted to the smallest numbered server that is still alive. The rerouting might require multiple hops through other servers, including those that have failed, to reach the smallest numbered alive server.

# If there are no alive servers to send the request to, then output -1 for that request.

# You need to handle a series of events, which can either be requests to servers or failures of servers. Based on these events, you should determine the correct server to route each request to.

# Input Format
# The first line contains an integer N, the number of servers.
# The second line contains an integer connections_rows, the number of connections.
# The third line contains an integer connections_columns, which is always 2.
# Each of the next connections_rows lines contain two integers, representing a connection between two servers.
# The next line contains an integer events_rows, the number of events.
# The next line contains an integer events_columns, which is always 2.
# Each of the next events_rows lines contains two integers. The first integer is either:
# indicating a request event followed by the server number.
# indicating a failure event followed by the server number.
# Constraints
# 1 <= N <= 1000
# 0<= connections_rows <= 1000
# 1<=events_rows<=100
# Events contain either a request (1) or failure (2) as the first integer.
# Output Format
# Return an integer array where each element corresponds to the rerouted server for each request event in the order they appear.
# Evaluation Parameters
# Sample Input
# 6
# 5
# 2
# 0 1
# 1 2
# 2 3
# 3 4
# 4 5
# 8
# 2
# 1 0
# 1 1
# 2 2
# 1 2
# 1 3
# 2 4
# 1 4
# 1 5
# Sample Output
# 0
# 1
# 0
# 3
# 0
# 5
# Explanation
# Request to server 0: Server 0 is alive, so the route is 0.
# Request to server 1: Server 1 is alive, so the route is 1.
# Failure of server 2: Server 2 is marked as failed.
# Request to server 2: Server 2 has failed. The request is rerouted to the next smallest alive server, which is 0.
# Request to server 3: Server 3 is alive, so the route is 3.
# Failure of server 4: Server 4 is marked as failed.
# Request to server 4: Server 4 has failed. The request is rerouted to the next smallest alive server, which is 0.
# Request to server 5: Server 5 is alive, so the route is 5.
# Execution time limit

