# -*- coding: utf-8 -*-

def main():
	n = int(input())

	for i in range(1,11):
		resultado = i * n
		print("{} x {} = {}".format(i,n,resultado))

if __name__ == '__main__':
	main()