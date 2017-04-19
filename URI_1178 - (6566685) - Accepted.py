# -*- coding: utf-8 -*-

def main():
    n = []
    x = float(input())
    n.append(x)
 
    for i in range(100):
        x = x / 2
        n.append(x)
 
    for i in range(100):
        print("N[{}] = {:.4f}".format(i,n[i]))
 
if __name__ == '__main__':
    main()