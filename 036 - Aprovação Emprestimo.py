# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.


val_imovel = float(input('Valor do Imóvel: R$ '))
salario = float(input('Salário: R$: '))
anos = int(input('Em quantos anos? '))
prestacao = val_imovel / (anos * 12)
minimo = salario * 30 / 100
print(f'A casa custa R${val_imovel} financiado em {anos} anos')
print(f'Pagará uma parcela de R${prestacao:.2f}')
if prestacao < minimo:
    print('APROVADO!')
else:
    print('NEGADO!')
