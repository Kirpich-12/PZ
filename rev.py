a = 'улыбок тебе дед макар'

def reverse(st:str)-> str:
    return st[::-1]

print(reverse(a))

def reverse_rc(st:str) -> str:
    if st == a[::-1]:
        return st
    else:
        st = st[-1] + st [:-1]
        return reverse_rc(st)

print(reverse_rc(a))