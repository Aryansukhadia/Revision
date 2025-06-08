def longest_balanced_subarray(arr):
    n = len(arr)
    max_len = 0

    for i in range(n):
        sum_pos = 0
        sum_neg = 0
        for j in range(i, n):
            if arr[j] > 0:
                sum_pos += arr[j]
            elif arr[j] < 0:
                sum_neg += arr[j]  

            if sum_pos + sum_neg == 0:
                length = j - i + 1
                if length > max_len:
                    max_len = length

    return max_len

n = int(input())
arr = [int(input()) for _ in range(n)]

print(longest_balanced_subarray(arr))
#the code finds the length of the longest subarray where the sum of positive and negative numbers is zero.