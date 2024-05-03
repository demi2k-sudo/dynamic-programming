def canSum(targetSum, numbers):
    table = [False for _ in range(targetSum+1)]
    table[0] = True
    # print(table)
    for i in range(targetSum+1):
        if table[i] == True:
            for j in numbers:
                if i+j<targetSum+1:
                    table[i+j] = True 
    # print(table)   
    return table[targetSum]

print(canSum(7,[2,3]))
print(canSum(8,[7,3]))
print(canSum(7,[5,3,4,7]))
print(canSum(8,[2,3,5]))
print(canSum(300,[7,14]))
        