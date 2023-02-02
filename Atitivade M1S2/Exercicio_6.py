#IMC = peso / ( altura )²
Peso = int(input('informe seu peso'))
Altura = float(input('informe sua altura'))
Resultado = Peso / Altura ** 2
print (Resultado)
if Resultado <=18.5:
    print ('Pessoa abaixo do peso')
if Resultado >=18.5 <=25.0:
    print ('Pessoa com peso normal')
if Resultado >=25.1 <=30.0:
    print('Pessoa acima do peso')
if Resultado >=30.1:
    print ('Pessoa Obesa')