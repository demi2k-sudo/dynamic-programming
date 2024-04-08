def bestSum(targetSum,numbers,memo=None):
    
    if memo is None:
        memo = {}
        
    if targetSum in list(memo.keys()):
        return memo[targetSum]
    
    if(targetSum==0):
        return []
    
    if(targetSum<0):
        return None
    
    shortest = None
    
    for i in numbers:
        res = bestSum(targetSum-i,numbers,memo)
        if(res is not None):
            res.append(i)
            if((shortest is None) or (len(shortest)>len(res))):
                shortest = res
    
    memo[targetSum] = shortest
    return shortest

print(bestSum(7,[5,3,4,7]))
print(bestSum(8,[2,3,5,7]))
print(bestSum(8,[2,5,7]))
print(bestSum(7,[2,3]))
print(bestSum(7,[2,4]))
print(bestSum(14,[7,14,1]))
# not possible
print(bestSum(300,[7,14]))