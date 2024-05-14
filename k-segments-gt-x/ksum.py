n = int(input("N:"))
k = int(input("K:"))
x = int(input("X:"))

arr = []

for i in range(n):
    arr.append(int(input()))
total = sum(arr)

def solve(k,x,arr,decisions=None,dummy=None,visited=[],answers=[]):
    
    
    if dummy is None:
        dummy = []   
        
    if decisions is None:
        decisions = [(m,g) for m,g in enumerate(arr)]

    if set(dummy) in visited:
        return

    visited.append(set(dummy))
    if sum([g for m,g in dummy])>=x and len(dummy)>=k:
        answers.append(dummy)
        
    for i in decisions:
        solve(k,x,arr,[m for m in decisions if m!=i],dummy+[i],visited,answers)
        
    return len(answers)


print(solve(k,x,arr))