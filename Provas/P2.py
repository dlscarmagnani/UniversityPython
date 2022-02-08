"""
Em Python crie um programa que atenda o menu a seguir. Desenvolva uma função para cada opção do menu. Utilize a criação de estruturas. Cadastrar 5 (vetor) vendas ( Tipo_Venda: cod_venda (int), dia(int), total(float), cliente (Tipo_Cliente: cod_cliente (int), nome(str) )
Menu de opções:

1 Cadastrar clientes

2 Mostrar todos os clientes

3 Cadastrar vendas

4 Mostrar todas as vendas

5 Mostrar o total de vendas de um determinado dia

6 Armazenar todos os campos da venda em um arquivo

7 Apresentar o conteúdo do arquivo

8 Sair

Observaçôes:

Na opção 4, as vendas podem ter o registro, por exemplo, uma venda dia 22, duas vendas no dia 23, outra venda no dia 21, outra venda no dia 15, mais uma venda no dia 15 e assim por diante

Na opção 5, o usuário do sistema informará/digitará o dia que quer e o sistema/programa fará uma pesquisa e calculará o total de vendas.

Na opção 6 e 7 o nome do arquivo deverá ser vendas.txt
"""

clientes = []
vendas = []

class tipocliente:
	codcliente = 0
	nome = ''

class tipovenda:
	codvenda = 0
	dia = 0
	total = 0.0

def menu():
	print('\nMenu de opções:')
	print('1. Cadastrar clientes.') #cadclient
	print('2. Mostrar todos os clientes') #allclient
	print('3. Cadastrar vendas.') #cadsale
	print('4. Mostrar todas as vendas.') #allsale
	print('5. Mostrar o total de vendas de um determinado dia.') #salesofday
	print('6. Armazenar todos os campos da venda em um arquivo.') #putinfile
	print('7. Apresentar o conteúdo do arquivo.') #showfile
	print('8. Sair.') #sair
	op = int(input('Digite a opção desejada: '))
	return op

def cadclient():
	p = tipocliente()
	p.codcliente = int(input('Código do cliente: '))
	p.nome = input('Nome do cliente: ')
	clientes.append(p)
	main()

def allclient():
	print('\nClientes cadastrados:')
	for tipocliente in clientes:
		p = tipocliente
		print(f'Cliente {p.codcliente}: {p.nome}.')
	main()

def cadsale():
	s = tipovenda()
	s.codvenda = int(input('Código da venda: '))
	s.dia = int(input('Dia da venda: '))
	s.total = float(input('Total da venda: R$ '))
	vendas.append(s)
	main()

def allsale():
	print('\nVendas cadastradas:')
	for tipovenda in vendas:
		s = tipovenda
		print(f'Venda código {s.codvenda}, realizada no dia {s.dia}. Total: R$ {s.total}.')
	main()

def salesofday():
	dia = int(input('Dia para consultar: '))
	print(f'\nVendas do dia {dia}:')
	for tipovenda in vendas:
		s = tipovenda
		if s.dia == dia:
			print(f'Venda código {s.codvenda}. Total: R$ {s.total}.')
		else:
			print('Nesse dia não houve vendas.')
	main()

def putinfile():
	arquivo = open('vendas.txt', 'a+')
	for tipovenda in vendas:
		s = tipovenda
		arquivo.write(f'{s.codvenda},{s.dia},{s.total}\n')
	arquivo.close()
	main()

def showfile():
	arquivo = open('vendas.txt', 'r')
	for line in arquivo.readlines():
		venda = line.split(",")
		print(f'Venda código {venda[0]}. Dia {venda[1]}. Total: R$ {venda[2]}.')
	arquivo.close()
	main()

def sair():
	print('\nTérmino da execução do programa.')

def main():
	opcao = menu()
	if opcao >= 1 and opcao <= 8:
		if opcao == 1:
			cadclient()
		elif opcao == 2:
			allclient()
		elif opcao == 3:
			cadsale()
		elif opcao == 4:
			allsale()
		elif opcao == 5:
			salesofday()
		elif opcao == 6:
			putinfile()
		elif opcao == 7:
			showfile()
		elif opcao == 8:
			sair()
	else:
		print('\nPor favor, digite uma opção de 1 a 8.')
		main()

main()