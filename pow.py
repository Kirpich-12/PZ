a = 2
b = 3

def pow(a:int, b:int)->int:
    if b == 0:
        return 1
    else:
        return a * pow(a, b  - 1)
    
print(pow(2, 3))