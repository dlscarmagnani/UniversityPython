"""
5. Faça um programa que realize o cadastro de contas bancarias com as seguintes informações: numero da conta, nome do titular e saldo. O banco permitirá o cadastramento de 15 contas. Crie uma função para cada opção do menu a seguir. Utilize a estrutura na passagem de parâmetro:
Menu de opções:

Cadastrar contas
Visualizar todas as contas
Consultar por nome
Alterar nome e/ou saldo de um número de conta
Excluir a conta com menor saldo
Sair
Observação:

No item de menu 4. Alterar nome e/ou saldo de um número de conta, entenda que apenas pode ser alterado o nome e o saldo depois que você pesquisar pelo número da conta.
No item 5 do menu, encontre o menor saldo dentre todos cadastrados, depois exclua esta ÚNICA conta.. O assunto de excluir algo de um vetor foi dado na disciplina de Algoritmo.

Percorra todo os vetor e quando a condição de enontrar um menor saldo for executada, guarde o índice
Fora do laço de repetição, exclua pelo índice, por exemplo com o comando pop(índice)
"""

geral = []
num_exis = []

class infos:
	nome = ''
	conta = 0
	saldo = 0.0

def menu():
	print('\nMenu de opções:')
	print('1. Cadastrar contas.') 
	print('2. Visualizar todas as contas.')
	print('3. Consultar por nome.')
	print('4. Alterar nome e/ou saldo de um número de conta.')
	print('5. Excluir a conta com menor saldo.')
	print('6. Sair.')
	op = int(input('Digite a opção desejada: '))
	return op

def cadastrar():
	p = infos()
	p.nome = input('Nome completo do titular: ')
	p.conta = int(input('Número da conta (sem hífen): '))
	p.saldo = float(input('Saldo: '))
	geral.append(p)
	num_exis.append(p.conta)
	main()

def todos():
	print('\nContas cadastradas:')
	for infos in geral:
		p = infos
		print(f'\nTitular: {p.nome}.')
		print(f'Conta: {p.conta}. Saldo: {p.saldo}.')
	main()

def consultar():
	nome = input('Nome para consultar: ')
	encontrado = False
	for infos in geral:
		p = infos
		if encontrado == False:
			if p.nome.lower() == nome.lower():
				print(f'\nCorrentista encontrado: {p.nome}.')
				print(f'Conta: {p.conta}. Saldo: {p.saldo}.')
				encontrado = True
	if encontrado == False:
		print('\nNome não encontrado.')
	main()

def alterar():
	account = int(input('Conta a ser alterada: '))
	aqui = None
	if account in num_exis:
		for i in range(len(geral)):
			if aqui == None:
				p = geral[i]
				if p.conta == account:
					aqui = i
		p = infos()
		p.conta = account
		p.nome = input('Novo titular: ')
		p.saldo = float(input('Novo saldo: '))
		geral[aqui] = p
		print('Conta atualizada com sucesso.')
	else:
		print('Conta inexistente.')
	main()

def excluirmenor():
	omenorsaldo = 0
	menorsaldo = None
	for i in range(len(geral)):
		p = geral[i]
		if menorsaldo == None:
			omenorsaldo = i
			menorsaldo = p.saldo
		elif p.saldo < menorsaldo:
			omenorsaldo = i
			menorsaldo = p.saldo
	excluir = geral[omenorsaldo]
	geral.remove(excluir)
	print(f'Conta {excluir.conta} excluída com sucesso.')
	main()

def sair():
	print('\nTérmino da execução do programa.')

def main():
	opcao = menu()
	if opcao >= 1 and opcao <= 6:
		if opcao == 1:
			cadastrar()
		elif opcao == 2:
			todos()
		elif opcao == 3:
			consultar()
		elif opcao == 4:
			alterar()
		elif opcao == 5:
			excluirmenor()
		elif opcao == 6:
			sair()
	else:
		print('\nPor favor, digite uma opção de 1 a 6.')
		main()

main()