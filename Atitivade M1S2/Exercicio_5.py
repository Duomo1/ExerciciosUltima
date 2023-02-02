from lzma import MF_BT2


Variavel1 = Gênero = int(input('Insira seu Gênero, 1. Para Homem, ou 2. Para Mulher'))
Variavel2 = altura = float(input('Insira sua altura'))
if Variavel1 == 1:
    print ((72.7 * altura)-58)
if Variavel1 == 2:
    print ((62.1 * altura)-44.7 )
