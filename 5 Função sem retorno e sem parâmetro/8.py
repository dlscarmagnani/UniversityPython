"""
8. (Função sem retorno sem parâmetro) Faça uma função/método que leia cinco valores inteiros, determine e mostre o maior e o menor deles. Não pode usar vetor e função pronta da linguagem Python.
"""

def verificar():
	cont = 0
	while cont < 5:
		n = int(input('Digite um número inteiro: '))
		if cont == 0:
			maior = menor = n
		else:
			if n > maior:
				maior = n
			if n < menor:
				menor = n
		cont += 1
	print(f'O maior número digitado foi {maior} e o menor número digitado foi {menor}.')

def main():
	verificar()

main()