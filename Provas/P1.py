"""
Não use nenhum método/função pronto da linguagem Python.

Desenvolva todas as funções a seguir:

a) Faça uma função com retorno (um valor no INSS calculado) e com parâmetro (um salario e alíquota de 9% do INSS) para calcular o imposto do INSS que é descontado de um funcionário.
b) Faça uma função com retorno (um salário líquido) e com parâmetro (um salario, um valor do INSS) que calcule o salário líquido de cada funionário.
c) Na função main() num laço de repetição, preencha um vetor de 10 funcionários. Em outro laço chame as outras funções (a e b) e apresente os salários orginais um por um, o valor que será desconto do INSS e salário líquido gerado.
"""

def inss(bruto, aliquota):
	return bruto * aliquota / 100

def liquido(bruto, aliquota):
	return bruto - inss(bruto, aliquota)

def main():
	print('Por favor informe o salário bruto de 10 funcionários e o sistema responderá com o valor do desconto (9% INSS) e o salário líquido:')
	for cont in range(10):
		bruto = float(input('\nSalário bruto: R$ '))
		aliquota = 9
		desc = inss(bruto, aliquota)
		liq = liquido(bruto, aliquota)
		print(f'Desconto INSS: R$ {desc:.2f}.')
		print(f'Salário líquido: R$ {liq:.2f}.')
	print(f'\nObrigado.')

main()