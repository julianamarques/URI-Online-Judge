# -*- coding: utf-8 -*-

def main():
	t1,t2,t3,t4 = map(int,input().split())

	total_tomadas = (t1 + t2 + t3 + t4) - 3

	print(total_tomadas)

if __name__ == '__main__':
	main()