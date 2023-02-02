class CaixaEletronico:
    
    def __init__(self, nome):
        self.notas = [100, 50, 20, 10]
        self.nome_banco = nome

    def sacar(self,valor_saque):
       #valor_maximo = 1000
        valor = valor_saque
        resto = -1
        notas_entregues = []
        #if valor > valor_maximo:
          #print ("saldo insuficiente")
        
        for valor_nota in self.notas:
            qtd_notas = valor // valor_nota
            resto = valor % valor_nota
            valor = resto
            
        if qtd_notas > 0:
            notas_entregues.append(f'\n{qtd_notas} NOTAS DE R$ {valor_nota},00 REAIS')

    def imprimir_resultado(self, notas_entregues):
        print(', '.join(notas_entregues))

if __name__ == '__main__':
    caixa_eletronico = CaixaEletronico('Ultima Bank')
    valor = int(input('Valor do saque: '))
    caixa_eletronico.sacar(valor)