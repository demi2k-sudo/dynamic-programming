def canConstruct(target,wordBank,memo=None):
    if memo is None:
        memo={}
    if target in list(memo.keys()):
        return memo[target]
    res = False
    if target=='':
        return True
    for i in wordBank:
        # print(f"checking with {i} target : {target}")
        if(i==target[:len(i)] or i==target):
            res = canConstruct(target[len(i):],wordBank,memo)
            memo[target] = res
            if(res):
                return res
    memo[target] = res
    return res

print(canConstruct("abcdef",["ab","abc","cd","def","abcd"]))
print(canConstruct("skateboard",["bo","rd","ate","t","ska","sk","ate"]))

# possible
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",["ee","eee","eeeeee","e","eeeee","eeeeeeee"]))



