def addi(g1, g2):
    return g1+g2
def subt(g1, g2):
    return g1-g2
def mult(g1, g2):
    return g1*g2
def divi(gi, g2):
    return g1/g2
def powe(g1, g2):
    return g1**g2
x=[0]
while True:
    n=input("1st Number (ans for previous answer)")
    p=int(input("2nd Number "))
    z=int(input("select calculation"))
    if n=="ans":
        k=x.pop()
        if (z == 1):
            k =addi(k, p)
            x.append(k)
        elif (z == 2):
            k =subt(k, p)
            x.append(k)
        elif (z == 3):
            k =k + mult(k, p)
            x.append(k)
        elif (z == 4):
            k =divi(k, p)
            x.append(k)
        elif (z == 5):
            k =powe(k, p)
            x.append(k)
        else:
            break
    else:
        l=int(n)
        x.pop()
        if (z == 1):
            k = addi(l, p)
            x.append(k)
        elif (z == 2):
            k = subt(l, p)
            x.append(k)
        elif (z == 3):
            k = mult(l, p)
            x.append(k)
        elif (z == 4):
            k = divi(l, p)
            x.append(k)
        elif (z == 5):
            k = powe(l, p)
            x.append(k)
        else:
            break
    print(x)