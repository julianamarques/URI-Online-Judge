# -*- coding: utf-8 -*-

def main():
    numero_funcionario = input()
    horas_trabalhadas = float(input())
    valor_hora = float(input())
  
    salario = horas_trabalhadas * valor_hora
  
    print ("NUMBER = {}".format(numero_funcionario))
  
    print ("SALARY = U$ {:.2f}".format(salario))
  
if __name__ == '__main__':
    main()