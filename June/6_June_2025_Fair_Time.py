# Problem 2 : Fair Time CODING SCORE: 10
# Problem Statement
# There are n fairs to be organized in the town. On a single day, you can only watch at most m
# fairs. You are given an array named a consisting of n elements denoting the price of the ticket of the
# i-th fair. Furthermore, the price of the ticket increases with each upcoming day. The price of the j-th
# ticket on the day d is (d * a ). You have to return an array of n elements whose i-th element
# denotes the minimum price of watching exactly i fairs.
# Input Format
# • The first line contains the integer n denoting the number of elements in the array a.
# • The next n lines contain the elements of the array a.
# • The last contains the integer m.
# Constraints
# • 2 <= n, a[i] <= 2*10
# • m < n
# Output Format
# • Return an array of n elements.
# Evaluation Parameters
# • Sample Input

# • Sample Output

# • Explanation
# For i=1, the best strategy is to purchase the ticket for the second fair on the first day.
# For i=2, the best strategy is to purchase tickets for the second and third fairs on the first day as
# m=2. So (3+4=7).

# i i j

# 5

# 5
# 6
# 3
# 4
# 7
# 8
# 2

# 3
# 7
# 16
# 27
# 44

# 48

# Powered by

# For i = 3, the best strategy would be to purchase the ticket for the first and third fair on the first day
# and the ticket for the second fair on the second day. So, total cost = 6+4 +(3*2)=16.
# For i = 4, the best strategy would be to purchase the ticket for the first and fourth fair on the first
# day and the ticket for the second and third fair on the second day. So, total cost = 6+7
# +(3*2)+(4*2)=27.
# For i = 5, one of the best strategies would be to purchase the ticket of:
# • The fourth and fifth fair on day 1.
# • The first and third fair on day 2.
# • The second fair is on day 3.
# The total cost of the ticket would be thus
# • = a * 1+ a *1 + a * 2+ a *2 + a *3
# • = 7*1 +8*1 + 6*1+4*2 + 3*3
# • = 44


def fairTime(a, m):
    n = len(a)
    a.sort()  # Sort prices to attend cheapest fairs first
    res = []
    
    for k in range(1, n + 1):  # for i = 1 to n fairs
        total_cost = 0
        for i in range(k):
            day = i // m + 1  # day number increases every m fairs
            total_cost += a[i] * day
        res.append(total_cost)
    
    return res

if __name__ == '__main__':
    a_count = int(input().strip())
    a = [int(input().strip()) for _ in range(a_count)]
    m = int(input().strip())
    
    result = fairTime(a, m)
    print('\n'.join(map(str, result)))
