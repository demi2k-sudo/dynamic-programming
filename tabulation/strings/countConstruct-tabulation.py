def countConstruct(target, wordBank):
    table = [0 for _ in range(len(target)+1)]
    table[0] = 1
    for i in range(len(target)+1):
        if table[i] >0:
            for j in wordBank:
                if i+len(j)<len(target)+1:
                    if target[i:i+len(j)] == j:
                        table[i+len(j)] += table[i]
                        # print(table)
    # print(table)      
    return table[-1]


print(countConstruct("abcdef",["ab","abc","cd","def","abcd"]))
print(countConstruct("purple",["purp","p","ur","le","purpl"]))
print(countConstruct("skateboard",["bo","rd","ate","t","ska","sk","ate"]))
print(countConstruct("enterapotentpot",["a","p","ent","enter","ot","o","t"]))
# possible
print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",["ee","eee","eeeeee","e","eeeee","eeeeeeee"]))
print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",["ee","eee","eeeeee","e","eeeee","eeeeeeee"]))
