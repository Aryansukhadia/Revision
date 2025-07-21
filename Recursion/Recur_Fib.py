def fib(n):
    if n==1 or n==0:
        return n
    fib_n_1 = fib(n-1)
    fin_n_2 = fib(n-2)
    output = fib_n_1+fin_n_2
    return output
n=4
print(fib(n))
#The default maximum recursion depth in Python is typically 1000 (function can call itself recursively). 
#This value can vary slightly between different Python versions or specific
# we can do import sys and sys.setrecursionlimit(3000)