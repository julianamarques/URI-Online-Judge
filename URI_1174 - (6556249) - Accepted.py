# -*- coding: utf-8 -*-

def main():
    a = []
 
    for i in range(100):
        x = float(input())
        a.append(x)
 
    for i in range(100):
        if a[i] <= 10:
            print("A[{}] = {}".format(i,a[i]))
 
if __name__ == '__main__':
    main()