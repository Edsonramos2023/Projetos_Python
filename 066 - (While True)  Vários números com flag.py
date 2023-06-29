# Crie um programa que leia números inteiros pelo teclado. O programa só
# vai parar quando o usuário digitar o valor "0", que é a condição de
# parada. No final, mostre quantos números foram digitados e qual foi a
# soma entre elas (desconsiderando o flag).

soma = cont = 0
while True:
    num = int(input('Números: '))
    if num <= 0:
        break
    soma += num
    cont += 1
print(f'Foi digitados {cont} valores e a soma é: {soma}')
