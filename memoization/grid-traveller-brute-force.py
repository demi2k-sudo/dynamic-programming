def gridTraveller(m,n):
    if(m==1 or n==1):
        return 1
    if (m==0 or n==0):
        return 0
    return gridTraveller(m-1,n) + gridTraveller(m,n-1)

print(gridTraveller(1,1))
print(gridTraveller(3,3))
print(gridTraveller(2,3))

# not possible
print(gridTraveller(18,18))