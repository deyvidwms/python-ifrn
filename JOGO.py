# -*- coding: utf-8 -*-

vogais = ['A','E', 'I', 'O', 'U']
vidas = 3
pontos = 0

# reposta: True/False
def jogada(letra, opcao):
	return letra in vogais and opcao == 'S'
def jogada2(letra, opcao):
	return letra in vogais and opcao == 'N'

while vidas > 0:
	nome = input("Digite um nome:")
	pos = int(input("Digite um pos"))
	letra = ' '
	if pos >= 0 and pos < len(nome):
		letra = nome[pos]

	opcao = ' '
	if letra != ' ':
		opcao = input ("Vogal(S/N)?")

	if jogada(letra, opcao):
	    pontos = pontos + 1
	    print ("Acertou!")
        elif jogada2(letra, opcao):
            pontos = pontos + 1
            print ("Acertou!")
	else:
		vidas = vidas - 1
		print ("Errou! Vidas(" ,vidas,")")

print ("Pontuação: ", pontos)
