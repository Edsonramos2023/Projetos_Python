# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6
# números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep
jogo = []
lista = []
quant_jog = int(input('Quantos jogos: '))
tot = 1
while tot <= quant_jog:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
            if cont >= 6:
                break

    lista.sort()
    jogo.append(lista[:])
    tot += 1
print('-'*6, f'SORTEANDO {quant_jog} JOGOS ', '-'*6)
for jogo, lista in enumerate(jogo):
    print(f'{jogo+1}ª Jogada: {lista}')
    sleep(1)
print('=='* 5, '< BOA SORTE >', '=='* 5)
