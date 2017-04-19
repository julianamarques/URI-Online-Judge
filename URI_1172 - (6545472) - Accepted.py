# -*- coding: utf-8 -*-

def main():
    x = []
 
    for i in range(10):
        n = int(input())
        x.append(n)
 
        if x[i] < 1:
            x[i] = 1
 
    for i in range(10):
        print ('X[{}] = {}'.format(i,x[i]))
 
if __name__ == '__main__':
    main()