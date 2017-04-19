# -*- coding: utf-8 -*-

def main():
    a = float(input())
    b = float(input())
  
    PESO_A = 3.5
    PESO_B = 7.5
  
    media = ((a * PESO_A) + (b * PESO_B)) / (PESO_A + PESO_B)
  
    print ("MEDIA = {:.5f}".format(media))
  
if __name__ == '__main__':
    main()