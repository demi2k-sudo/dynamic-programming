def howSum(targetSum,numbers):
    if(targetSum==0):
        return []
    if(targetSum<0):
        return None
    for i in numbers:
        res = howSum(targetSum-i,numbers)
        if( res is not None):
            res.append(i)
            return res
    return None

print(howSum(7,[2,3]))
print(howSum(7,[5,3,4,7]))
print(howSum(7,[2,4]))

# not possible
print(howSum(300,[7,14]))