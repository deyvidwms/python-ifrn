# -*- coding: utf-8 -*-
aluno = ('Romerito','SP','20','Corrida','Futebol')

nome = aluno[0]
print(nome)

for elem in aluno:
    print(elem)

print("Tamanho: ", len(aluno))

# não pode -> (aluno[0] = "Gustavo")
# Tupla não modifica.

print( type (aluno))
