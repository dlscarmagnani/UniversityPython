"""
9. (Função sem retorno sem parâmetro) Faça uma função/método que leia um valor inteiro e positivo N e mostre o valor de S, obtido pelo seguinte cálculo:
S = 1 + 1/1! + 1/2! + 1/3! + ... + 1/N!
Observvação: Não pode usar vetor e função pronta da linguagem Python.

Digite seu código aqui.

S = 1 + 1 + 1/2! + 1/3!
S = 1 + 1 + 0.5 + 0.16
S = 2.66
"""

def verificar():
	N = int(input('Informe um número inteiro maior que zero: '))
	S = 1
	for n in range(1,N+1):
		fat = 1
		fatorial = 1
		while fat <= n:
			fatorial = fatorial * fat
			fat = fat + 1
		S = S + 1 / fatorial
	print(f'A expressão matemática de S resultou em {S:.2f}')
 
def main():
	verificar()

main()