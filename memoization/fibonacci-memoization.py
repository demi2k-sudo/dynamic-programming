def fibonacci(n,memo={}):
    if n in list(memo.keys()):
        return memo[n]
        
    if(n<2):
        memo[n] = n
        return n
    memo[n] = fibonacci(n-1,memo)+fibonacci(n-2,memo)
    return memo[n]


print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))


print(fibonacci(50))
