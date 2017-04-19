# -*- coding: utf-8 -*-

def main():
	lista_peca1 = input().split()
	lista_peca2 = input().split()

	cod_peca1 = int(lista_peca1[0])
	quant_peca1 = int(lista_peca1[1])
	valor_peca1 = float(lista_peca1[2])

	cod_peca2 = int(lista_peca2[0])
	quant_peca2 = int(lista_peca2[1])
	valor_peca2 = float(lista_peca2[2])

	total = (quant_peca1 * valor_peca1) + (quant_peca2 * valor_peca2)

	print("VALOR A PAGAR: R$ {:.2f}".format(total))

if __name__ == '__main__':
	main()