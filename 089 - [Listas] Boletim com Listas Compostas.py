# Crie um programa que leia nome e duas notas de vários alunos e guarde
# tudo em uma lista composta. No final, mostre um boletim contendo
# a média de cada um e permita que o usuário possa mostrar as
# notas de cada aluno individualmente.


ficha = []

while True:
    nome = str(input('Nome: '))
    nota_01 = float(input('Nota 1: '))
    nota_02 = float(input('Nota 2: '))
    media = nota_01 + nota_02 / 2
    ficha.append([nome, [nota_01, nota_02], media])
    while True:
        resp = str(input('Continuar?[S/N] ')).upper()[0]
        if resp in 'S/N':
            break
    if resp in 'N':
        break
print(f'{"ALUNO":<4} {"NOME":<10}{"MÉDIA":>4}')
for i, v in enumerate(ficha):
    print(f'{i+1}º Nome: {v[0]:<10} Média: {v[2]:>4.1f} ')
while True:
    opção = int(input('Dgite 999 PARA ENCERRAR: '))
    if opção == 999:
        break
    if opção <= len(ficha)-1:
        print(f'Nota de {ficha[opção][0]} são {ficha[opção][1]}')
print('FIM')