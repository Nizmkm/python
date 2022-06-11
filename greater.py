a=int(input('first number'))
b=int(input('second number'))
c=int(input('third number'))
if a>b:
    if a>c:
        print(a,'is greater')
    else:
        print(c,'is greater')
elif b>c :
    print(b,'is greater')
else:
    print(c,'is greater')
