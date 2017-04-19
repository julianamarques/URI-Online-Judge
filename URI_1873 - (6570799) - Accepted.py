# -*- coding: utf-8 -*-

def main():
    n = int(input())
    x = []
  
    for i in range(n):
        lista = input()
        x = lista.split()
  
        raj = x[0]
        sheldon = x[1]
  
        if raj == "tesoura" and sheldon == "papel":
            print("rajesh")
  
        elif raj == "papel" and sheldon == "pedra":
            print("rajesh")
  
        elif raj == "pedra" and sheldon == "lagarto":
            print("rajesh")
  
        elif raj == "lagarto" and sheldon == "spock":
            print("rajesh")
  
        elif raj == "spock" and sheldon == "tesoura":
            print("rajesh")
  
        elif raj == 'tesoura' and sheldon == "lagarto":
            print("rajesh")
  
        elif raj == "lagarto" and sheldon == "papel":
            print("rajesh")
  
        elif raj == "papel" and sheldon == "spock":
            print("rajesh")
  
        elif raj == "spock" and sheldon == "pedra":
            print("rajesh")
  
        elif raj == "pedra" and sheldon == "tesoura":
            print("rajesh")
  
        elif raj == sheldon:
            print("empate")
  
        else:
            print("sheldon")
  
if __name__ == '__main__':
    main()