# -*- coding: utf-8 -*-

def main():
    n = []
  
    for i in range(20):
        y = input()
        n.append(y)
 
    n.reverse()
 
    for i in range(20):
        print ('N[{}] = {}'.format(i,n[i]))
 
if __name__ == '__main__':
    main()