## O programa abaixo deve calcular a média dos valores digitados pelo usuário.
## No entanto, ele não está funcionando bem. Você pode consertá-lo?

# def calcular_media(valores):
#    tamanho = 1
#    soma = 0.0
#    for i, valor in enumerate(valores):
#        soma += valor
#        i += 1
#    media = soma / tamanho

# continuar = True
# valores = []
# while continuar:
#    valor = input('Digite um número para entrar na sua média ou "ok" para calcular o valor:')
#    if valor.lower() == 'ok':
#        continuar = False

# media = calcular_media(valores)
# print('A média calculada para os valores {} foi de {}'.format(valores, media))



def calcular_media(valores):
    tamanho = len(valores)
    soma = sum(valores)
    media = soma / tamanho
    return media

continuar = True
valores = []

while continuar:
    valor = input('Digite um número para entrar na sua média ou "ok" para calcular o valor: ')
    if valor.lower() == 'ok':
        continuar = False
    else:
        valores.append(float(valor))

media = calcular_media(valores)
print('A média calculada para os valores {} foi de {}'.format(valores, media))


#Principais correções realizadas:

#Substituí "false" por "False" para corrigir o erro de sintaxe.
#Adicionei else na estrutura condicional para garantir que apenas valores diferentes de "ok" sejam adicionados à lista.
#Utilizei float(valor) para garantir que os valores digitados sejam tratados como números decimais.
#Substituí enumerate por len e sum para calcular o tamanho da lista e a soma dos valores de forma mais eficiente.
#Incluí um retorno na função calcular_media para que ela retorne o valor calculado.