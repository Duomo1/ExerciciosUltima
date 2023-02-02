def decorador (function):
    def apresentacao (*args, **kwargs):
        print('Código para verificação se o número é ímpar ou par.')
        function (*args, **kwargs)
    return apresentacao

@decorador
def verificacao (numero):
    resultado = numero % 2
    if resultado == 0:
        print ('O número é par')
    else:
        print ('O número é ímpar')
numero = int(input('Insira um número'))
verificacao(numero)
