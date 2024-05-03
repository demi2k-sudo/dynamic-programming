import numpy as np

def gridTraveller(m,n):
    table = np.zeros((m+1,n+1))
    table[1][1] = 1
    # print(table)
    for i in range(m+1):
        for j in range(n+1):
            if j+1<n+1:
                table[i][j+1]+=table[i][j]
            if i+1<m+1:
                table[i+1][j]+=table[i][j]
    # print(table)
    return int(table[m][n])
    
print(gridTraveller(1,1))
print(gridTraveller(2,3))
print(gridTraveller(3,2))
print(gridTraveller(3,3))
print(gridTraveller(18,18))