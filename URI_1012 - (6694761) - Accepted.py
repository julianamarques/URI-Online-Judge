# -*- coding: utf-8 -*-

def main():
	lista_valores = input().split()

	a = float(lista_valores[0])
	b = float(lista_valores[1])
	c = float(lista_valores[2])

	PI = 3.14159

	area_triang_retang = a * c / 2
	area_circulo = PI * c**2
	area_trapezio = ((a + b) * c) / 2
	area_quadrado = b * b
	area_retangulo = a * b

	print("TRIANGULO: {:.3f}".format(area_triang_retang))
	print("CIRCULO: {:.3f}".format(area_circulo))
	print("TRAPEZIO: {:.3f}".format(area_trapezio))
	print("QUADRADO: {:.3f}".format(area_quadrado))
	print("RETANGULO: {:.3f}".format(area_retangulo)) 

if __name__ == '__main__':
	main()