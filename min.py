a = 0
Max_l = [1,2,5,8]

def Max(a:list):
    if len(a) == 0:
        return 0
    return a[0] if a[0] > Max(a[1:]) else Max(a[1:])

print(Max(Max_l))