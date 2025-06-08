import math

N = int(input())
arr = [int(input()) for _ in range(N)]

sum_arr = sum(arr)
mean = sum_arr / N

target_mean = 2 * mean

x = target_mean * (N + 1) - sum_arr
print(math.ceil(x))

#the code calculates the minimum value of x that needs to be added to the array such that the new mean becomes double the original mean. 
# It uses the formula derived from the relationship between the sum, mean, and number of elements in the array. 
# The result is printed as the ceiling value of x.