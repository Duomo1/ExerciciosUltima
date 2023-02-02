def retorno(**kwargs):
       funcao(**kwargs)
    return retorno

Número =  int(input('Insira um número:'))
resultado = Número % 2
if resultado == 0:
    print ('O número é par')
else:
    print ('O número é ímpar')