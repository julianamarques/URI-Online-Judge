# -*- coding: utf-8 -*-

def main():
    x = []
  
    lista = input()
  
    x = lista.split()
  
    a = x[0]
    b = x[1]
    c = x[2]
    d = x[3]
  
    if (int(b) > int(c)) and (int(d) > int(a)) and ((int(c) + int(d)) > (int(a) + int(b))) and (int(c) > 0) and (int(d) > 0) and (int(a) % 2 == 0):
        print ('Valores aceitos')
  
    else:
        print ('Valores nao aceitos')
  
if __name__ == '__main__':
    main()