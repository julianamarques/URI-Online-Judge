# -*- coding: utf-8 -*-

def main():
    livros = []
 
    while True:
        try:
            n = int(input())
        except:
            break
 
        for i in range(n):
            codigos = input()
            livros.append(codigos)
 
            if len(livros) == n:
                livros.sort()
                 
                for i in range(len(livros)):
                    print("{}".format(livros[i]))
 
                livros = []
 
if __name__ == '__main__':
    main()