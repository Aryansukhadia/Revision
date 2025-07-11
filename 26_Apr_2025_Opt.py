# Optimizing Print Efficiency
# subject Codingcasino
# Description
# Problem Statement

# You own a Xerox shop and take pride in your time management skills. A customer arrives with N files to be printed, and each file 'files[i]' indicates the time it takes to print. With your k printer machines, the objective is to create an optimal assignment, ensuring the minimum possible maximum working time among all machines.

# The working time of any machine is defined as the sum of the time it takes to complete all files assigned to it. Your task is to devise an efficient strategy to allocate files to machines, aiming to minimize the maximum working time.

# Input Format

# The First line of input contains an integer k. 
# The Second line of input contains an integer n (length of files). 
# The next n line of input contains an integer.
# Constraints

# 1 <= k <= files.length <= 12
# 1 <= files[i] <= 107
# Output Format

# It will be an integer, which is the minimum possible maximum working time among all machines.
# Sample test case

# Input

# 2
# 5
# 1
# 2
# 4
# 7
# 8
# Output

# 11
# Explanation

# As given k=2 (print machine) , n=5 , files = [1,2,4,7,8]

# print_machine '1' : files[0] , files[1] ,files[4] => 1+2+8 =11

# print_machine '2' : files[2]+files[3] => 4+7 => 11

# The minimum possible maximum working time among all machines is 11.

# Execution time limit

# show less
# checkPartially accepted
# Show quality annotations
# Python 3
# 
# Evaluation details
# check
# Testcase #1 (sample)
# Status
# Passed
# Execution time
# 0.00s
# CPU
# 0s
# Memory
# 116kB
# Description
# Testcase passed! The solution's output matches the expected output.
# Input
# 2
# 5
# 1
# 2
# 4
# 7
# 8
# Expected output
# 11

# def minimumTimeRequired(k, files):
#     files.sort(reverse=True)  # Big files first to prune faster

#     def canDistribute(index, machines, limit):
#         if index == len(files):
#             return True
#         for i in range(k):
#             if machines[i] + files[index] <= limit:
#                 machines[i] += files[index]
#                 if canDistribute(index + 1, machines, limit):
#                     return True
#                 machines[i] -= files[index]
#             if machines[i] == 0:
#                 break
#         return False

#     left, right = max(files), sum(files)
#     while left < right:
#         mid = (left + right) // 2
#         if canDistribute(0, [0] * k, mid):
#             right = mid
#         else:
#             left = mid + 1
#     return left
