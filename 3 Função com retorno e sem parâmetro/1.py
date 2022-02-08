"""
1. (Função com retorno sem parâmetro) Faça um programa contendo uma função/método que verifique se um número é par, retorne mostrando a str/string ‘É par’ ou se ‘É ímpar’.
"""

def par_ou_impar():
	num = int(input('Inform um número: '))
	if num % 2 == 0:
		return 'É par'
	else:
		return 'É ímpar'

def main():
	print(par_ou_impar())

main()