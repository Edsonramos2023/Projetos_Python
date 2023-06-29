# Crie um programa que leia o nome e o preço de vários produtos. O programa
# deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.


soma = tot_mil = cont = menor = 0
barato = ' '
while True:
    produto = str(input('Nome do Produto: '))
    valor = float(input('Valor: R$'))
    soma += valor
    cont += 1

    if valor >= 1000:
        tot_mil += 1

    if cont == 1 or valor < menor:
        menor = valor
        barato = produto

    while True:
        resp = str(input('Continuar? [S/N] ')).upper()[0]
        if resp in 'S/N':
            break
        print('INVÁLIDO! Apenas S ou N')
    if resp in 'N':
        break

print(f'O total da compra é R${soma:.2f}')
print(f'Tem {tot_mil} produtos com valor á cima de R$1000.00')
print(f'Produto mais barato é: {barato} custando R${menor:.2f}')
