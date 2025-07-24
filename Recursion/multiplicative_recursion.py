def multiplicative_recursion(m,n):
    if n==1:
        return m
    else:
        return m+ multiplicative_recursion(m,n-1)
m=5
n=4
print(multiplicative_recursion(4,5))