"""
4. (Função sem retorno sem parâmetro) Faça uma função/método que leia um único valor representado em segundos, converta-o e apresente o resultado em horas, minutos e segundos.

h = segundos / 3600
r = resto(segundos / 3600)
m = r / 60
s = resto(r / 60)
Observação 1: resto de uma divisão em Python %.
Observação 2: a hora, o minuto e o segundo devem ser apresentados como números inteiros.
"""

def calcular_horas():
	segundos = int(input('Informe um valor: '))
	h = segundos / 3600
	r = segundos % 3600
	m = r / 60
	s = r % 60
	print('Hora:',h//1,'Minuto:',m//1,'Segundo:',s)

def main():
	calcular_horas()

main()