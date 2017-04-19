# -*- coding: utf-8 -*-

def main():
	raio = float(input())
	PI = 3.14159
	
	volume = ((4.0 / 3) * PI * raio ** 3)

	print("VOLUME = {:.3f}".format(volume))

if __name__ == '__main__':
	main()