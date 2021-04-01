# -*- coding: utf-8 -*-

#dicionários
notas = {'nota1' : 10, 'nota2' : 9}
n = notas['nota1']
#print (n)

notas['nota2'] = 9.5
n = notas['nota2']
#print(n)
#print(notas)

alunos = {1: 'Giovanni', 2: 'Ana', 3: 'Paula'}

chaves = list(alunos.keys())
valores = list(alunos.values())
elementos = list(alunos.items())
# print (chaves)
# print (valores)
# print (elementos)


#for nome in alunos.values():
#    print(nome)



#ifrn = {}
#print (type(ifrn))


#for i in range(3):
#    ifrn[i] = input("Digite seu nome: ")

#print (ifrn)

ifrn = {0 : 'jose'}

print (ifrn)

ifrn[1] = 'romerito'

print (ifrn)

ifrn['huehuehue'] = 'chave misturada'
print (ifrn)
