def allConstruct(target, wordBank, memo=None):
    if memo is None:
        memo = {}
        
    if target in list(memo.keys()):
        return memo[target]
        
    if target == "":
        return [[]]
    
    final = []
    
    for i in wordBank:
        if target[:len(i)] == i or target == i:
            res = allConstruct(target[len(i):],wordBank,memo)
            for j in res:
                j.insert(0,i)
            final+=res
    memo[target] = final
    return final

print(allConstruct("abcdef",["ab","abc","cd","def","ef","abcd"]))
print(allConstruct("purple",["purp","p","ur","le","purpl"]))
print(allConstruct("skateboard",["bo","rd","ate","t","ska","sk","ate"]))

# possible
print(allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",["ee","eee","eeeeee","e","eeeee","eeeeeeee"]))
print(allConstruct("eeeeeeeeef",["eee","eeeeee","f"]))