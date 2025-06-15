from collections import Counter

def is_palindromic_anagram(s):
    freq = Counter(s)
    odd_count = sum(1 for count in freq.values() if count % 2 != 0)
    return "YES" if odd_count <= 1 else "NO"

# This code defines a function to check if a string can be rearranged to form a palindrome.
# It uses the Counter class from the collections module to count the frequency of each character in the string.
# A string can be rearranged into a palindrome if at most one character has an odd frequency.
# If the count of characters with odd frequencies is 0 or 1, it returns "YES"; otherwise, it returns "NO".
