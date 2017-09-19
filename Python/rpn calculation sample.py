j=[]
while True:
    x=input()
    if x=="+":
        a=j.pop()
        b=j.pop()
        c=a+b
        j.append(c)
        print(j)
    elif x=="-":
        a=j.pop()
        b=j.pop()
        c=a-b
        j.append(c)
        print(j)
    elif x=="*":
        a=j.pop()
        b=j.pop()
        c=a*b
        j.append(c)
        print(j)
    elif x=="/":
        a = j.pop()
        b = j.pop()
        c = a + b
        j.append(c)
        print(j)
    else:
        d=int(x)
        j.append(d)
        print(j)