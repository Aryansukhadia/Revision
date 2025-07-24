def count_zeros_builtin(n):
    return str(abs(n)).count('0')
n=1000
print(count_zeros_builtin(n))

def count_zeros_recursive(n):
    # Base case: if n is 0, it has 1 zero
    if n == 0:
        return 1
    # Recursive helper function to handle general case
    def helper(n):
        if n == 0:
            return 0
        if n % 10 == 0:
            return 1 + helper(n // 10)
        else:
            return helper(n // 10)
    
    return helper(abs(n))
n=1000
print(count_zeros_recursive(n))