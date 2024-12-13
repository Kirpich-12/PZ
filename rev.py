a = 'улыбок тебе дед макар'

def reverse(st:str)-> str:
    return st[::-1]

print(reverse(a))

def reverse_rc(st:str) -> str:
    if len(st) == 1:
       return st
    return reverse_rc(st[1:]) + st[0]
print(reverse_rc(a))