def longest_prefix(strs):
    prefix = ""
    if len(strs) == 0: return prefix
    
    smallest = float('INF')
    for i in range(len(strs)):
        smallest = min(smallest, len(strs[i]))
    
    for i in range(smallest):
        for j in range(len(strs)): 
            if strs[0][i] != strs[j][i]:
                return prefix
        prefix += strs[0][i]

    return prefix

strs = list(input().split())

#strs = ['dog', 'racecar', 'car']
#strs = ['flower', 'flow', 'flight']

print(longest_prefix(strs))