# -*- coding: utf-8 -*-

def main():
    cartas = []
    carta = input()
 
    cartas = carta.split()
 
    a = cartas[0]
    b = cartas[1]
 
    if int(a) > int(b):
        print("{}".format(a))
 
    else:
        print("{}".format(b))
  
if __name__ == '__main__':
    main()