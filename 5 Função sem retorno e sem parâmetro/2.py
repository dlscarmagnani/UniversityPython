"""
2. (Função sem retorno sem parâmetro) Faça uma função/método que leia dois valores positivos e apresente a soma dos N números existentes entre eles (inclusive).
"""

def verificar():
	soma = 0
	i = int(input('Informe um número: '))
	f = int(input('Informe outro número: '))
	while i <= f:
		soma = soma + i
		i += 1
	print(f'A soma é: {soma}')

def main():
	verificar()

main()