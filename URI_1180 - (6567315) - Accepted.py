# -*- coding: utf-8 -*-

def main():
    x = []
    n = int(input())
    lista = input()
    x = lista.split()
    menor = int(x[0])
    posicao = 0
 
    for i in range(n):
        if int(x[i]) < int(menor):
            menor = int(x[i])
            posicao = i
        
    print ('Menor valor: {}'.format(menor))
    print ('Posicao: {}'.format(posicao))
     
if __name__ == '__main__':
    main()