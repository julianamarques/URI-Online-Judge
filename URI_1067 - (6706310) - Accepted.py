# -*- coding: utf-8 -*-

def main():
	x = int(input())

	for i in range(1,x+1):
		if i % 2 != 0:
			print(i)

if __name__ == '__main__':
	main()