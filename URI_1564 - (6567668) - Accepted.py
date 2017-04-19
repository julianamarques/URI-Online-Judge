# -*- coding: utf-8 -*-

def main():
    x = []
 
    while True:
        try:
            n = input()
        except:
            break
 
        if n == "0":
            print("vai ter copa!")
 
        elif n >= "1":
            print("vai ter duas!")
 
if __name__ == '__main__':
    main()