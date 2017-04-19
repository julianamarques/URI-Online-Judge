# -*- coding: utf-8 -*-

def main():
    nome = input()
    salario = float(input())
    valor_vendas = float(input())
 
    comissao = valor_vendas * 0.15
 
    salario = salario + comissao
 
    print("TOTAL = R$ {:.2f}".format(salario))
 
if __name__ == '__main__':
    main()