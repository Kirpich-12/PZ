a = 8

def fibonacci(a):
    if a == 0 : 
       # print(a)
        return 0
    elif a == 1 : 
       # print(a)
        return 1
    return fibonacci(a-1)+fibonacci(a-2)



print(fibonacci(a))