
#À vista em dinheiro, recebe 15% de desconto
#À vista no cartão de crédito, recebe 10% de desconto
#Em duas vezes, preço normal de etiqueta sem juros
#Mais de duas vezes, preço normal de etiqueta mais juros de 10%


Variavel1 = Valor_de_etiqueta = int(input('Valor da Etiqueta'))
Variavel2 = Forma_de_pagamento = int(input('Forma de pagamento, 1. Para À vista em dinheiro, 2. Para À vista no Cartão de Crédito, 3. Para 2x Sem Juros, 4. Para mais de 2x com juros de 10%'))
if Forma_de_pagamento == 1:
    print('R$', Valor_de_etiqueta - 15*Valor_de_etiqueta/100)
if Forma_de_pagamento == 2:
    print('R$', Valor_de_etiqueta - 10*Valor_de_etiqueta/100)
if Forma_de_pagamento == 3:
    print('R$', Valor_de_etiqueta)
if Forma_de_pagamento == 4:
    print('R$', Valor_de_etiqueta + 10*Valor_de_etiqueta/100)