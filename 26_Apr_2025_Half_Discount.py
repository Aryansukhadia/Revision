
# Half Discount
# subject Codingcasino
# Description
# Problem Statement

# You are given a graph of Cities. The cities are numbered from 1 to N. You are in the City 1. You have M routes, which come along with a cost. You have a special talent where you get the cost of the routes you move in. Find the maximum cost you can acquire by moving from City 1 to City N.

# Note: You can assume that it's always possible to reach from City 1 to City N. However, if you can get an arbitrarily large score, return −1.

# Input Format

# The first line contains an integer N, the total number of Cities.
# The second line contains an integer M, the total number of routes.
# The third line contains an integer 3, representing that there will be 3 integers in the next M lines.
# The next M lines contains 3 integers A B C - representing a route from A to B with a cost of C.
# Output Format

# The maximum cost you can acquire by moving from City 1 to City N.
# Constraints

# 1 ≤ N ≤ 2500
# 1 ≤ M ≤ 5000
# 1 ≤ A , B ≤ N
# -1000000000 ≤ C ≤ 1000000000
# Evaluation Parameters

# Sample Input
# 4 
# 5
# 3
# 1 2 3
# 2 4 -1
# 1 3 -2
# 3 4 7
# 1 4 4
# Sample Output
# 5
# Explanation


# If we see the graph, The maximum Cost we can acquire is 5, We can move from 1 to 3 and 3 to 4, that will give the maximum cost.

# Execution time limit

