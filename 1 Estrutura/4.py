"""
4. Uma escola precisa montar o cadastro geral de seus alunos. Este cadastro deverá conter as seguintes informações por aluno: nome completo, data de nascimento, telefone, endereço e série atual. Levando em conta que esta escola possui no máximo 500 alunos, como você faria para estruturar estas informações num sistema de gerenciamento para a escola? Implemente utilizando estrutura. Também use a criação de funções para cada operação. Use o menu a seguir:
Menu de opções:

Cadastrar alunos
Consulta por nome
Visualizar todos os dados
Sair
"""

geral = []

class infos:
	nome = ''
	dn = ''
	telefone = ''
	endereco = ''
	serie = 0

def menu():
	print('\nMenu de opções:')
	print('1. Cadastrar aluno.') 
	print('2. Consulta por nome.')
	print('3. Visualizar todos os dados.')
	print('4. Sair.')
	op = int(input('Digite a opção desejada: '))
	return op

def cadastrar():
	p = infos()
	p.nome = input('Nome completo: ')
	p.dn = input('Data de nascimento (DD/MM/AAA): ')
	p.telefone = input('Telefone (XX 9XXXX-XXXX): ')
	p.endereco = input('Endereço: ')
	p.serie = int(input('Série: '))
	geral.append(p)
	main()

def consultar():
	nome = input('Nome para consultar: ')
	encontrado = False
	for infos in geral:
		p = infos
		if encontrado == False:
			if p.nome.lower() == nome.lower():
				print(f'\nAluno encontrado: {p.nome}, {p.serie}ª Série.')
				print(f'Data de nascimento: {p.dn}. Telefone: {p.telefone}.')
				print(f'Endereço: {p.endereco}.')
				encontrado = True
	if encontrado == False:
		print('\nAluno não encontrado.')
	main()

def todos():
	print('\nAlunos cadastrados:')
	for infos in geral:
		p = infos
		print(f'\nAluno: {p.nome}, {p.serie}ª Série.')
		print(f'Data de nascimento: {p.dn}. Telefone: {p.telefone}.')
		print(f'Endereço: {p.endereco}.')
	main()

def sair():
	print('\nTérmino da execução do programa.')

def main():
	opcao = menu()
	if opcao >= 1 and opcao <= 4:
		if opcao == 1:
			cadastrar()
		elif opcao == 2:
			consultar()
		elif opcao == 3:
			todos()
		elif opcao == 4:
			sair()
	else:
		print('\nPor favor, digite uma opção de 1 a 4.')
		main()

main()