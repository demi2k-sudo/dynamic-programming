def canConstruct(target,wordBank):
    res = False
    if target=='':
        return True
    for i in wordBank:
        # print(f"checking with {i} target : {target}")
        if(i==target[:len(i)] or i==target):
            res = canConstruct(target[len(i):],wordBank)
            if(res):
                return res
    return res

print(canConstruct("abcdef",["ab","abc","cd","def","abcd"]))
print(canConstruct("skateboard",["bo","rd","ate","t","ska","sk","ate"]))

# not possible
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",["ee","eee","eeeeee","e","eeeee","eeeeeeee"]))



