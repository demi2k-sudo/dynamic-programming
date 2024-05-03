def allConstruct(target, wordBank):
    
    table = [None for _ in range(len(target)+1)]
    table[0] = [[]]
    
    for i in range(len(target)+1):
        # print('asd')
        if table[i] is not None:
            for j in wordBank:
                # print('dsa')
                if len(j)+i<len(target)+1:
                    if target[i:len(j)+i] == j:
                        # print(1)
                        temp = [combination + [j] for combination in table[i]]
                        # print(2)
                        if table[i+len(j)] is None:
                            table[i+len(j)] = temp
                        else:
                            table[i+len(j)] += temp
                        # print(table)
    return table[-1]                        
                                         






print(allConstruct("abcdef",["ab","abc","cd","def","ef","abcd","c"]))
print(allConstruct("purple",["purp","p","ur","le","purpl"]))
print(allConstruct("skateboard",["bo","rd","ate","t","ska","sk","ate"]))
print(allConstruct("aaaaaaaaaaz",["a","aa","aaa","aaaa","aaaaa"]))
# possible
# print(allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",["ee","eee","eeeeee","e","eeeee","eeeeeeee"]))
print(allConstruct("eeeeeeeeef",["eee","eeeeee","f"]))