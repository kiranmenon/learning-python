

def permutations(items):
    n = len(items)
    if n==0: yield []
    else:
        for i in range(n):
            #print("items[:i] :- ")
            #print(items[:i])
            #print("items[i+1:] :- ")
            #print(items[i+1:])
            for cc in permutations(items[:i] + items[i+1:]):
                #print("[items[i]]:")
                #print([items[i]])
                #print("cc:") 
                #print(cc)
                yield [items[i]] + cc

for p in permutations(['r','e','d']): print(''.join(p))

