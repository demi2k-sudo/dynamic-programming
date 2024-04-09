def countConstruct(target,wordBank,memo=None):
    
    if memo is None:
        memo = {}
    
    if target in list(memo.keys()):
        return memo[target]
    
    sum = 0
    if target == "":
        return 1
    
    for i in wordBank:
        if target[:len(i)] == i or target==i:
            # print(f'target:{target} sum:{sum} value:{i}')
            sum+=countConstruct(target[len(i):],wordBank,memo)
    memo[target] = sum    
    return sum

print(countConstruct("abcdef",["ab","abc","cd","def","abcd"]))
print(countConstruct("purple",["purp","p","ur","le","purpl"]))
print(countConstruct("skateboard",["bo","rd","ate","t","ska","sk","ate"]))
print(countConstruct("enterapotentpot",["a","p","ent","enter","ot","o","t"]))
# possible
print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",["ee","eee","eeeeee","e","eeeee","eeeeeeee"]))
print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",["ee","eee","eeeeee","e","eeeee","eeeeeeee"]))
