def menu():
    print ("1-Media Aritimetica")
    print ("2-Media Ponderada")
    print ("3-Sair")
    op = int(input("opcao"))
    return op

op = menu()
while menu() != 3:
    if op == 1:
        print("Media Simp")
    elif op == 2:
        print("Media Pond")
    op = menu()
