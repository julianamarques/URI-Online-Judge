# -*- coding: utf-8 -*-

def main():
	cod,quant = input().split()
	total = 0.00

	if cod == "1":
		total = int(quant) * 4.00

	elif cod == "2":
		total = int(quant) * 4.50

	elif cod == "3":
		total = int(quant) * 5.00

	elif cod == "4":
		total = int(quant) * 2.00

	elif cod == "5":
		total = int(quant) * 1.50

	print("Total: R$ {:.2f}".format(total))

if __name__ == '__main__':
	main()