"""
3. Elabore uma estrutura para representar um produto (código, nome, preço). Crie uma função para cadastrar 5 produtos. Crie outra função para aplicar 10% de aumento no preço do produto e apresente, por meio de outra função, todos os dados do produtos cadastrados, após o aumento.
"""

class TipoProduto:
	codigo = 0
	nome = ''
	preco = 0.0

def cadastro(produto):
	for i in range(5):
		p = TipoProduto()
		p.codigo = int(input('Cadastre o código do produto: '))
		p.nome = input('Cadastre o nome do produto: ')
		p.preco = float(input('Cadastre o preço do produto: R$ '))
		produto.append(p)
	
def aumento(produto):
	for i in range(len(produto)):
		produto[i].preco = produto[i].preco * 1.1
	
def apresentar(produto,aumento):
	for i in range(len(produto)):
		print(f'Código: {produto[i].codigo}. \tNome: {produto[i].nome}. \tPreço + 10%: R$ {produto[i].preco:.2f}.')

def main():
	produto = []
	cadastro(produto)
	aumento(produto)
	apresentar(produto,aumento)

main()