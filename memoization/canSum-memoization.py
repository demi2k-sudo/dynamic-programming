def canSum(targetSum, numbers, memo=None):
    
    # if initialized as memo={}, then it is shared among the neighbor function calls
    if memo is None:
        memo={}
    
    if(targetSum in list(memo.keys())):
        return memo[targetSum]
    
    if(targetSum==0):
        return True
    if(targetSum<0):
        return False
    
    for i in numbers:
        if(canSum(targetSum-i,numbers,memo) == True):
            memo[targetSum] = True
            return True
        
    memo[targetSum] = False
    return False

print(canSum(7,[2,3]))
print(canSum(8,[7,3]))
print(canSum(7,[5,3,4,7]))
print(canSum(8,[2,3,5]))


# not possible
print(canSum(300,[7,14]))
        