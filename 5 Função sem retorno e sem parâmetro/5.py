"""
5. (Função sem retorno sem parâmetro) Faça uma função/método que receba o preço antigo e atual de um produto, determine o percentual de acréscimo entre esses valores e apresente-o.

r = (100 * preco_novo - 100 * preco_antigo) / preco_antigo
"""

def percentual():
	
	preco_antigo = float(input('Preço antigo: R$ '))
	preco_atual = float(input('Preço atual: R$ '))

	percentual_aumento = ((preco_atual / preco_antigo) * 100) - 100
	
	print(f'Houve {percentual_aumento}% de aumento.')

def main():
	percentual()

main()