"""
1. Elabore uma estrutura para representar um produto (código, nome, preço). Aplique 10% de aumento no preço do produto e apresente.
"""

def TipoProduto():
	codigo = int(input('Cadastre o código do produto: '))
	nome = input('Cadastre o nome do produto: ')
	preco = float(input('Cadastre o preço do produto: R$ '))

	preco_final = preco * 1.1

	print(f'O preço do {nome} (código {codigo}) com 10% de aumento é de R$ {preco_final:.2f}.')

def main():
	TipoProduto()

main()