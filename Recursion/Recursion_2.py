def sum_n(n):
    if n==0:
        return 0
    small_o = sum_n(n-1)
    output = small_o+ n
    return output
n=int(input())
print(sum_n(n))
