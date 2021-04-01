lista = []
numero = int (input("Digite: "))
letraa = 0
letrab = 0
letrabsoma = 0
letrac = 0
letrad = 0
letradcont = 0

while numero != 201:
    lista.append(numero)
    if numero < 70:
        letraa += 1
    if 100 <= numero <= 200:
        letrabsoma += numero
        lerab += 1
    if 50 <= numero <= 150:
        letrac += 1
    if numero < 50:
        letrad += 1
        if numero == 10 or numero == 20:       
            letradcont += 1
    numero = int(input("Digite: "))

print(letraa)
print(letrabsoma/letrab)
print((len(lista)*letrac)/100.0)
print((letradcont * letrad)/100.0)
