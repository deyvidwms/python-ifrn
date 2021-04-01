A = int(input("Digite o valor Limite da lista 1: "))
B = int(input("Digite o valor Limite da lista 2: "))
L1 = []
L2 = []
def funf(L1,L2):
    L1 = list(range(25,A,25))
    L2 = list(range(15,B,15))

    return "Lista 1: ", L1, "Lista 2: ", L2

print(funf(L1,L2))
