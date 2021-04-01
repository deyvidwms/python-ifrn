a = int(input("Digite o valor A: "))
b = int(input("Digite o valor B: "))
c = int(input("Digite o valor C: "))
n = int(input("Digite o valor N: "))
def fermat (a,b,c,n):
    if ((a**n)+(b**n)) == (c**n):
        print ("O teorema está correto!")
    else:
        print ("O teorema não está correto!")
    return

(fermat(a,b,c,n))

