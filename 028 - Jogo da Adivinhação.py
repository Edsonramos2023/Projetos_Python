# Escreva um programa que faça o computador "pensar" em um número inteiro
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
# escolhido pelo computador. O programa deverá escrever na tela se o
# usuário venceu ou perdeu.

from random import randint

pc = randint(0, 5 )
print('Estou pensando em um número de 0 a 5...')
jogador = int(input('um número: '))
if pc == jogador:
    print('jogador venceu')
else:
    print('Pc venceu')
print(f'PC pensou: {pc} eu EU: {jogador}')
