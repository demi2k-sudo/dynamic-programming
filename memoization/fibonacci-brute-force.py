def fibonacci(n):
    if(n<2):
        return n
    return fibonacci(n-1)+fibonacci(n-2)


print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))

#this will not be possible
print(fibonacci(50))
