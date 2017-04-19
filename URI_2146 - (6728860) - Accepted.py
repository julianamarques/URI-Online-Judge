# -*- coding: utf-8 -*-

def main():
	while True:
		try:
			n = int(input())
		except:
			break
		
		print(n - 1)

if __name__ == '__main__':
	main()