def howSum(targetSum, numbers):
    table = [None for _ in range(targetSum+1)]
    table[0] = []
    for i in range(targetSum+1):
        if table[i] is not None:
            for j in numbers:
                if i+j < targetSum+1:
                    table[i+j] = table[i] + [j]
                    # table[i+j].append(j)
    return table[targetSum]


print(howSum(7, [2, 3]))
print(howSum(7, [5, 3, 4, 7]))
print(howSum(7, [2, 4]))
print(howSum(300, [1, 7, 14]))

print(howSum(300, [7, 14]))
