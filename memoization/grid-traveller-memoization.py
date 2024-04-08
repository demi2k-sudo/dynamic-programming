def gridTraveller(m,n,memo={}):
    key = str(m) + ',' + str(n)
    
    if(key in list(memo.keys())):
        return memo[key]
    
    if(m==1 or n==1):
        memo[key] = 1
        return 1
    
    if (m==0 or n==0):
        memo[key] = 0
        return 0
    
    memo[key] =  gridTraveller(m-1,n) + gridTraveller(m,n-1)
    return memo[key]
    
print(gridTraveller(1,1))
print(gridTraveller(3,3))
print(gridTraveller(2,3))


print(gridTraveller(18,18))