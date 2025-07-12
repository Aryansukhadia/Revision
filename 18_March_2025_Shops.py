# Special Discount
# subject Codingcasino
# Description
# Problem Statement
# Steve has two strings, str1 and str2. He got an amazing discount of 5000 Rs on a product, but the condition is that both strings must be the same. Now, he wishes to make str1 the same as str2, but there is a problem: he can only modify his string using the given operations any number of times. For each operation, he needs to pay 5 Rs, which will be deducted from the discount price. The operations are:

# Insert 1 character anywhere in the string.
# Remove 1 character from anywhere in the string.
# Change 1 character in the string.
# Help Steve change str1 to str2 so that he gets the maximum discount. If the discount becomes less than zero while performing these operations, return 0.

# Input Format
# First line contains string str1.
# Next line contains string str2.
# Constraints
# 1<=|str1|, |str2|<=1000. Contains small case English alphabets.
# Output Format

# Return an integer denoting the maximum discount Steve will get.
# Sample Testcase
# Sample Input
# doselect
# selecd
# Sample Output
# 4985
# Explanation
# First we need to remove D and O of str1 after that we will change last T of str1 to D.

# We need total 3 operation which cost 15Rs. So the remaining discount is 5000-15 = 4985.

# Execution time limit

def minimumOperations(str1, str2):
    n = len(str1)
    m = len(str2)
    
    # Create a DP table with dimensions (n+1) x (m+1)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Fill the base cases
    for i in range(n + 1):
        dp[i][0] = i  # i deletions
    for j in range(m + 1):
        dp[0][j] = j  # j insertions

    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # characters match
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],    # remove
                    dp[i][j - 1],    # insert
                    dp[i - 1][j - 1] # replace
                )

    operations = dp[n][m]
    discount = 5000 - operations * 5
    return max(discount, 0)

if __name__ == '__main__':
    str1 = input()
    str2 = input()
    result = minimumOperations(str1, str2)
    print(result)
