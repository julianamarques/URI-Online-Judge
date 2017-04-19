# -*- coding: utf-8 -*-

def main():
    lista = []
 
    while True:
        try:
            nome = input()
        except:
            break
 
        lista.append(nome)
 
    for i in range(1,len(lista)):
        atual = i
 
        while (atual > 0) and (lista[atual - 1].lower() > lista[atual].lower()):
            lista[atual - 1],lista[atual] = lista[atual],lista[atual - 1]
            atual -= 1
 
    print("{}".format(lista[-1]))
 
if __name__ == '__main__':
    main()