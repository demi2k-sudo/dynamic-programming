def allConstruct(target, wordBank):
    
    if target == "":
        return [[]]
    
    final = []
    
    for i in wordBank:
        if target[:len(i)] == i or target == i:
            res = allConstruct(target[len(i):],wordBank)
            for j in res:
                j.insert(0,i)
            final+=res
    return final

print(allConstruct("abcdef",["ab","abc","cd","def","ef","abcd"]))
print(allConstruct("purple",["purp","p","ur","le","purpl"]))
print(allConstruct("skateboard",["bo","rd","ate","t","ska","sk","ate"]))

# not possible
print(allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",["ee","eee","eeeeee","e","eeeee","eeeeeeee"]))