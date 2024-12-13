a = 'а роза упала на лапу Азора'

def pal(tst:str) -> bool:
    tst = tst.replace(' ','')
    tst = tst.lower()
    if len(tst) == 1 or len(tst) == 0:
        return True
    else:
        if tst[0] == tst[-1]:
            return pal(tst[1:-1])
        else:
            return False 

print(pal(a))