"""
2. (Função com retorno sem parâmetro) Faça um programa contendo uma função/método que verifique se um número é par, retorne/mostre o valor bool True para par e False para ímpar.
"""

def func():
	n = int(input('Digite um número: '))
	if n % 2 == 0:
		return True
	else:
		return False
 
def main():
	print('Este programa apresenta se um número é par ou ímpar.....\n\n')
	if func():	# se	func() é verdadeira		 if func() == True:
		print('Este valor é par')
	else:
		print('Este valor é ímpar')
 
main()