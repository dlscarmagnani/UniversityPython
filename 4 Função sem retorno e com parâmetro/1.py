"""
1. (Função sem retorno com parâmetro) Faça uma função/método para a partir de um preço de um produto informado, calcular e apresentar o novo preço reajustado em alguma porcentagem que deve ser informada (digitada) pelo usuário.
"""

def calcular_aumento(preco, porcentagem): # parâmetros
		aumento = preco + (preco * porcentagem / 100)
		print('O preço do produto após o aumento é', aumento)

def main():
		preco_produto = float(input('Informe o preço do produto: '))
		porcentagem = float(input('Informe a porcentagem: '))
		calcular_aumento(preco_produto, porcentagem)

main()