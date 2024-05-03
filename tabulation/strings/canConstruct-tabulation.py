def canConstruct(target, wordBank):
    table = [False for _ in range(len(target)+1)]
    table[0] = True
    for i in range(len(target)+1):
        if table[i] == True:
            for j in wordBank:
                if i+len(j)<len(target)+1:
                    if target[i:i+len(j)] == j:
                        table[i+len(j)] = True
    # print(table)      
    return table[-1] 
     

print(canConstruct("abcdef",["ab","abc","cd","def","abcd"]))
print(canConstruct("abcdef",["ab","d","def","abcd"]))
print(canConstruct("skateboard",["bo","rd","ate","t","ska","sk","ate"]))
print(canConstruct("enterapotentpot",["a","p","ent","enter","ot","o","t"]))

# possible
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",["ee","eee","eeeeee","e","eeeee","eeeeeeee"]))



