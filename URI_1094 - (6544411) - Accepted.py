# -*- coding: utf-8 -*-

def main():
    n = input()
    
    total = 0
    coelho = 0
    rato = 0
    sapo = 0
 
    for i in range(n):
        x = raw_input()
        quantia, tipo = x.split()
 
        total = total + int(quantia)#
 
        if tipo == 'C':
            coelho = coelho + int(quantia)
 
        elif tipo == 'R':
            rato  = rato + int(quantia)
 
        elif tipo == 'S':
            sapo  = sapo + int(quantia)
 
    perc_coelho = (coelho * 100.00) / total
    perc_rato = (rato * 100.00) / total
    perc_sapo = (sapo * 100.00) / total
 
    print 'Total: {} cobaias'.format(total)
    print 'Total de coelhos: {}'.format(coelho)
    print 'Total de ratos: {}'.format(rato)
    print 'Total de sapos: {}'.format(sapo)
 
    print 'Percentual de coelhos: %.2f %%' % (perc_coelho)
    print 'Percentual de ratos: %.2f %%' % (perc_rato)
    print 'Percentual de sapos: %.2f %%' % (perc_sapo)
    
if __name__ == '__main__':
    main()