#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

vc = float(input('Qual o valor do imóvel? R$ '))
sal = float(input('Qual o salário do comprador? R$ '))
anos = int(input('Em quantos anos deseja pagar? '))
prestacao = vc / (anos * 12)
max = sal * 30 / 100
print('-=' * 30)
print('Para pagar uma casa de R$ {:.2f} em {} anos...'.format(vc, anos))
print('-=' *30)
if prestacao < max:
    print('Empréstimo CONCEDIDO!')
    print('Sua prestação será de R$ {:.2f} mensais.'.format(prestacao))
elif prestacao == max:
    print('Empréstimo CONCEDIDO!')
    print('Sua prestação será de R$ {:.2f} mensais.'.format(prestacao))
    print('ATENÇÃO: VOCÊ ESTÁ COMPROMETENDO 30% DO SEU SALÁRIO!!')
else:
    print('Empréstimo NEGADO!')
    print('Sua prestação passaria de R$ {:.2f} mensais.\nO que seria mais de 30% do seu salário.'.format(prestacao))
    