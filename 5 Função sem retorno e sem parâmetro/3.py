"""
3. (Função sem retorno sem parâmetro) Faça uma função/método que receba três números inteiros a, b, c que sejam divisíveis por a. O valores b e c representam o intervalo da estrutura de repetição. Apresente a quantidade e os números divisíveis. Não pode usar vetor e função pronta da linguagem Python.
"""

def verificar():

	dvs = ''
	qtde = 0

	print('Digite abaixo três números inteiros (a, b e c):')
	a = int(input('a) '))
	b = int(input('b) '))
	c = int(input('c) '))

	for i in range(b, c+1):
		if i % a == 0:
			qtde += 1
			dvs += str(i) + ', '

	print(f'Números divisíveis por a: {dvs}.')
	print(f'Quantidade de números divisíveis por a: {qtde}.')

def main():
	verificar()

main()