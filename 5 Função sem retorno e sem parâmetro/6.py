"""
6. (Função sem retorno sem parâmetro) Faça uma função/método que leia um valor inteiro entre 1 e 9 e mostre a seguinte tabela de multiplicação
"""

def ta():
	n = int(input('Informe um número entre 1 e 9: '))
  
	for i in range(1, n+1):
		for j in range(1, i+1):
			r = i * j
			print(r, end='\t')
		print()

def main():
	ta()

main()