# -*- coding: utf-8 -*-

def main():
    while True:
        x = []
 
        lista = input()
        x = lista.split()
 
        for i in range(len(x)):
            x[i] = int(x[i])
 
        m = x[0]
        n = x[1]
 
        soma = m + n
        resultado = str(soma)
 
        if lista == "0 0":
            break
 
        print("{}".format(resultado.replace("0","")))
 
if __name__ == '__main__':
    main()