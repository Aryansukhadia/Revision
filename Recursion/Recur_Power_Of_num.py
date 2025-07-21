def mul_n(n,x):
    if n==0:
        return 1
    return x*mul_n(n-1,x)

x=int(input())
n=int(input())
print(mul_n(n,x))