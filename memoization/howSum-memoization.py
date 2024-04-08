def howSum(targetSum,numbers,memo=None):
    
    if memo is None:
        memo = {}
        
    if targetSum in list(memo.keys()):
        return memo[targetSum]
        
    if(targetSum==0):
        return []
    
    if(targetSum<0):
        return None
    
    for i in numbers:
        res = howSum(targetSum-i,numbers,memo)
        if( res is not None):
            res.append(i)
            memo[targetSum] = res
            return res
    
    memo[targetSum] = None
    return None

print(howSum(7,[2,3]))
print(howSum(7,[5,3,4,7]))
print(howSum(7,[2,4]))
print(howSum(300,[1,7,14]))
# not possible
print(howSum(300,[7,14]))