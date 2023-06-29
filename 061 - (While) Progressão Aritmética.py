#  Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
#  mostrando os 10 primeiros termos da progressão usando a estrutura While.

print('====-- PROGRESSÃO ARITIMÉTICA --===')
primeiro = int(input('Primeiro termo da PA: '))
razão = int(input('Termo: '))
termo = primeiro
c = 0
while c < 10:
    print(f'{termo}→ ', end='')
    termo += razão
    c += 1
print('FIM')
