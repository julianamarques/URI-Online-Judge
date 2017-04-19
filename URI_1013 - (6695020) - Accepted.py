# -*- coding: utf-8 -*-

def main():
	numeros = input().split()

	a = int(numeros[0])
	b = int(numeros[1])
	c = int(numeros[2])

	if a > b and a > c:
		print("{} eh o maior".format(a))

	elif b > a and b > c:
		print("{} eh o maior".format(b))

	elif c > a and c > b:
		print("{} eh o maior".format(c))

if __name__ == '__main__':
	main()