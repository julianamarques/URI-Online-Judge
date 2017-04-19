# -*- coding: utf-8 -*-

def main():
    raio = float(input())
 
    PI = 3.14159
 
    area = PI * (raio ** 2)
 
    print("A={:.4f}".format(area))
 
if __name__ == '__main__':
    main()