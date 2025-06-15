def longest_ego_line(pairs):
    pairs.sort(key=lambda x: x[0])
    n = len(pairs)
    dp = [1] * n  
    for i in range(n):
        for j in range(i):
            if pairs[i][0] > pairs[j][1]: 
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)
#this code defines a function to find the length of the longest "ego line" in a list of pairs,
# where each pair consists of two integers (a, b).
# It uses dynamic programming to build up the solution by checking pairs of elements and ensuring that the first element of one pair is greater than the second element of another pair.
