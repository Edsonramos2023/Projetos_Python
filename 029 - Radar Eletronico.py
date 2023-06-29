# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Informe a velocidade: '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print('Você excedeu o limite da rodovia de 80Km/h')
    print(f'Pagará uma multa de R${multa:.2f}')
else:
    print('Parabéns, está dentro do limite.')
    