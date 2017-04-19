# -*- coding: utf-8 -*-

def main():
    lista = input().split()
 
    s = int(lista[0])
    t = int(lista[1])
    f = int(lista[2])
 
    hora_chegada = s + t + f
 
    if hora_chegada >= 24:
        hora_chegada = hora_chegada - 24
 
    elif hora_chegada < 0:
        hora_chegada = hora_chegada + 24
 
    print("{}".format(abs(hora_chegada)))
 
if __name__ == '__main__':
    main()