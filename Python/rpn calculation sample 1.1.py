def plus():
    q = h.pop()
    r = h.pop()
    z=q+r
    h.append(z)
def minus():
    q = h.pop()
    r = h.pop()
    z=q-r
    h.append(z)
def multi():
    q = h.pop()
    r = h.pop()
    z=q*r
    h.append(z)
def divid():
    q = h.pop()
    r = h.pop()
    z=q/r
    h.append(z)
def power():
    q = h.pop()
    r = h.pop()
    z=q**r
    h.append(z)
h=[]
while True:
    x=input("Enter the number or operator")
    if x.isdigit()==True:
        x=int(x)
        h.append(x)
    else:
        if x=="+":
            plus()
        elif x=="-":
            minus()
        elif x=="*":
            multi()
        elif x=="/":
            divid()
        elif x=="^":
            power()
        else:
            print("Syntax Error")
    print(h)

