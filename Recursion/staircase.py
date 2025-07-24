def climbing_stairs(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    elif n==2:
        return 2
    dp=[0]*(n+1)
    # a,b,c=1,1,2
    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]
        # temp = a+b+c
        # a,b,c=b,c,temp
    # return c 

n=5
print(climbing_stairs(n))