# -*- coding: utf-8 -*-

def main():
    a = float(input())
    b = float(input())
    c = float(input())
  
    PESO_A = 2
    PESO_B = 3
    PESO_C = 5
  
    media = ((a * PESO_A) + (b * PESO_B) + (c * PESO_C)) / (PESO_A + PESO_B + PESO_C)
  
    print ("MEDIA = {:.1f}".format(media))
  
if __name__ == '__main__':
    main()