"""
7. (Função sem retorno sem parâmetro) Faça uma função/método que leia uma hora de início e de término de um jogo, ambas divididas em dois valores distintos: hora e minuto. Deverá ser apresentado a duração expressa em minutos, considerando que o tempo máximo de duração de um jogo é de 24 horas e que ele pode começar em um dia e terminar no outro.
"""

def verificar():
	print('Digite o horário inicial e o horário final de um jogo, separados em horas e minutos:')
	h_i = int(input('Hora inicial: '))
	m_i = int(input('Minuto inicial: '))
	h_f = int(input('Hora final: '))
	m_f = int(input('Minuto final: '))
	tot_i = (h_i * 60) + m_i
	tot_f = (h_f * 60) + m_f
	if tot_i > tot_f:
		total = ((24 * 60) - tot_i) + tot_f
	if tot_i < tot_f:
		total = tot_f - tot_i
	print(f'A duração total do jogo foi de {total} minutos.')

def main():
	verificar()

main()