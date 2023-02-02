def conta (string, letra):
    contador = 0
    for item in string:
        if item == letra:
            contador += 1
    return contador
string = str(input('Insira a palavra a ser contada'))
letra = str(input('Qual a letra a ser contada.'))
print (conta(string, letra))
