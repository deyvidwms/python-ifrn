# tabuada

def tabuada (N):
    print("Tabuada de {}".format(N))
    lista = []
    for  i in range(1,11):
        res = N * i
        # criação de tuplas
        elemento = (N,i,res)
        lista.append(elemento)
        #print ("{} * {} = {}".format(N, i, res))

    return lista

        
        
valor = int(input("Digite um valor:"))
resultado = tabuada(valor)
print (resultado)
