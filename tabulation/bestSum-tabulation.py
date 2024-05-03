def bestSum(targetSum, numbers):
    table = [None for _ in range(targetSum+1)]
    table[0] = []
    for i in range(targetSum+1):
        if table[i] is not None:
            for j in numbers:
                if i+j < targetSum+1:
                    if table[i+j] is not None:
                        if len(table[i+j])>len(table[i]+[j]):
                            table[i+j] = table[i] + [j]
                    else:        
                        table[i+j] = table[i] + [j]
                    # table[i+j].append(j)
    return table[targetSum]


print(bestSum(7, [2, 3, 5]))
print(bestSum(7, [5, 3, 4, 7]))
print(bestSum(8, [1, 4, 5]))
print(bestSum(100,[1,2,5,25]))
print(bestSum(300, [1, 7, 14]))

print(bestSum(300, [7, 14]))
