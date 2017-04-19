# -*- coding: utf-8 -*-

def main():
    idade = 0
    soma = 0.00
    media = 0.00
    quant = 0

    while True:
    	idade = int(input())

    	if idade >= 0:
    		soma = soma + idade
    		quant += 1

    	elif idade < 0:
    		break

    media = soma / quant
    print("{:.2f}".format(media))
 
if __name__ == '__main__':
    main()