# -*- coding: utf-8 -*-

def main():
	n = int(input())

	for i in range(1,10001):
		if i % n == 2:
			print(i)

if __name__ == '__main__':
	main()