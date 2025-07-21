def min_removals_to_find_min_max(arr):
    n = len(arr)
    min_idx = arr.index(min(arr))
    max_idx = arr.index(max(arr))

    op1 = max(min_idx, max_idx) + 1
    op2 = max(n - min_idx, n - max_idx)
    op3 = min(min_idx + 1 + (n - max_idx), max_idx + 1 + (n - min_idx))

    return min(op1, op2, op3)

n = int(input())
arr = [int(input()) for _ in range(n)]
#this code defines a function to calculate the minimum number of removals needed to find both the minimum and maximum elements in an array
# considering different strategies for removing elements from either end of the array. 
# It then reads an integer n and an array of n integers from input, and prints the result of the function.