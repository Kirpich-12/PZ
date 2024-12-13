a = [1, 2, 3, 4, 5]

def count(ls:list):
    if len(ls) == 1:
        return int(ls[0])
    ls[0] += ls[-1]
    return count(ls[:-1])

print(count(a))
    
