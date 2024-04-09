def countConstruct(target,wordBank):
    
    sum = 0
    if target == "":
        return 1
    
    for i in wordBank:
        if target[:len(i)] == i or target==i:
            # print(f'target:{target} sum:{sum} value:{i}')
            sum+=countConstruct(target[len(i):],wordBank)
    
    return sum

print(countConstruct("abcdef",["ab","abc","cd","def","abcd"]))
print(countConstruct("purple",["purp","p","ur","le","purpl"]))
print(countConstruct("skateboard",["bo","rd","ate","t","ska","sk","ate"]))

# not possible
print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",["ee","eee","eeeeee","e","eeeee","eeeeeeee"]))
