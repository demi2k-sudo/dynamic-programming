import numpy as np

def fibonacci(n):
    table = np.zeros(n+3).tolist()
    table[0] = 0
    table[1] = 1
    for i in range(n+1):
        table[i+1] +=table[i]
        table[i+2] =+table[i]
    return table[n]

print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(6))

print(fibonacci(50))