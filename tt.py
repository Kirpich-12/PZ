st = '12345'
a  = '12345'
for i in range(5):
    if st == a[::-1]:
        print(st)
    else:
        st = st[1:] + st [:-1]
    print(st)