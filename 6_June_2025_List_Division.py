# Problem 3 : List Division CODING SCORE: 10
# Problem Statement
# In a small town, a group of friends love playing with numbers. They have a task to complete,
# assigned by their math teacher, Mr Johnson. He gives each friend a list of integers and says, "Your
# mission is to divide this list into two halves. The first half consists of numbers less than zero, and
# the second half contains numbers greater than zero. Remember, there should be no zeros. You can
# change the element of the list with any integer." Your task is to determine the minimum number of
# elements that need to change.
# Input Format
# • The first line will contain an integer N, denoting the total element in the list.
# • Next N lines will contain elements of the list.
# Constraints
# • 1<=N<=10
# • -10 <=listElement <=10
# Output Format
# • Return an integer denoting the minimum elements that need to change.
# Evaluation Parameters
# Sample Input

# Sample Output

# Explanation
# Replace element[1] with -10
# Replace element[4] with 2
# Replace element[5] with 3
# now element = [-8, -10, -10, 2, 2, 3, 8, 2]
# so we need minimum 3 elements to be replaced.
# Solution REJECTED SCORE: 0.0 / 10


def divideList(elements):
    n = len(elements)
    half = n // 2
    changes = 0

    # First half: must be negative
    for i in range(half):
        if elements[i] >= 0:
            changes += 1

    # Second half: must be positive
    for i in range(half, n):
        if elements[i] <= 0:
            changes += 1

    return changes

if __name__ == '__main__':
    elements_count = int(input().strip())
    elements = [int(input().strip()) for _ in range(elements_count)]
    result = divideList(elements)
    print(result)
