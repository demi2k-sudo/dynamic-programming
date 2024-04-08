def canSum(targetSum, numbers):
    
    if(targetSum==0):
        return True
    if(targetSum<0):
        return False
    
    for i in numbers:
        if(canSum(targetSum-i,numbers)):
            return True
    return False

print(canSum(7,[2,3]))
print(canSum(7,[5,3,4,7]))
print(canSum(8,[2,3,5]))
print(canSum(8,[7,3]))

# not possible
print(canSum(300,[7,14]))
        