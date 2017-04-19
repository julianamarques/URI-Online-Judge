# -*- coding: utf-8 -*-

def main():
    while True:
        velocidades = []
 
        try:
            l = int(input())
        except:
            break
 
        v = input()
        velocidades = v.split()
 
        for i in range(len(velocidades)):
            velocidades[i] = int(velocidades[i])
 
        if max(velocidades) < 10:
            print("1")
 
        elif max(velocidades) >= 20:
            print("3")
 
        elif max(velocidades) >= 10 or max(velocidades) < 20:
            print("2")
 
if __name__ == '__main__':
    main()