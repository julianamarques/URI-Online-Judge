# -*- coding: utf-8 -*-

def main():
    fib = []
    t = int(input())
 
    primeiro = 0
    segundo = 1
    proximo = 0
    fib.append(primeiro)
 
    for i in range(t):
        n = int(input())
        for i in range(n+1):
            primeiro = segundo + proximo
            segundo = proximo
            proximo = primeiro
            fib.append(proximo)
 
        print("Fib({}) = {}".format(n,fib[i]))
 
if __name__ == '__main__':
    main()