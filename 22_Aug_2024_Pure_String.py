# Pure String
# subject Codingcasino
# Description
# Problem Statement

# Given a name, find out the number of ways to remove exactly one sub-string so that all the remaining characters are the same. This means the number of distinct characters left should be 1 or 0. You should remove at least one character; if you remove the whole string, it is still correct.

# Since the value can be very large, return the modulo of the result by 109+7.

# Note: The string contains at least two distinct characters.

# Input Format

# The first line contains the string stn.
# The characters of the string are in lowercase English alphabets.
# Constraints

# 2<=len(stn)<=105
# Output Format

# Return the integer as per the problem statement.
# Evaluation Parameters

# Sample Input
# abaa
# Sample Output
# 6
# Explanation
# The remaining part can be counted as equal if you remove the following substrings.

# The parts are stn[1:2], stn[1:3], stn[1:4], stn[2:2], stn[2:3], stn[2:4].

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pureString' function below.
# 
# The function is expected to return a LONG INTEGER.
# The function accepts STRING stn as parameter.
#

def pureString(stn):
    MOD = 10**9 + 7
    n = len(stn)
    total = 0

    # Precompute prefix count for each position
    prefix_freq = [0] * 26
    freq_prefix_list = []
    for ch in stn:
        prefix_freq[ord(ch) - ord('a')] += 1
        freq_prefix_list.append(prefix_freq[:])  # store copy

    # Precompute suffix count from each position
    suffix_freq = [0] * 26
    freq_suffix_list = [None] * n
    for i in range(n-1, -1, -1):
        suffix_freq[ord(stn[i]) - ord('a')] += 1
        freq_suffix_list[i] = suffix_freq[:]

    # Try all substrings s[i:j+1] to remove
    for i in range(n):
        for j in range(i, n):
            # Remaining = s[0:i] + s[j+1:]
            remaining_freq = [0] * 26

            if i > 0:
                for k in range(26):
                    remaining_freq[k] += freq_prefix_list[i-1][k]
            if j + 1 < n:
                for k in range(26):
                    remaining_freq[k] += freq_suffix_list[j+1][k]

            # Count distinct characters
            distinct = sum(1 for val in remaining_freq if val > 0)
            if distinct <= 1:
                total = (total + 1) % MOD

    return total

if __name__ == '__main__':
    stn = input()
    result = pureString(stn)
    print(str(result))
