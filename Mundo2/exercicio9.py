#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#à vista dinheiro/cheque: 10% de desconto

#à vista no cartão: 5% de desconto

#em até 2x no cartão: preço formal 

#3x ou mais no cartão: 20% de juros

preco_normal = float(input('Digite o valor do produto: R$ '))
print('Escolha a forma de pagamento: ')
print('[1] À vista: Dinheiro/Débito/Pix.')
print('[2] Em 2x no cartão de crédito.')
print('[3] Em 3x ou mais no cartão de crédito.')
opcao = int(input('Digite a opção desejada: '))
if opcao == 1:
    preco_final = preco_normal * 0.95
    print('O valor a ser pago é: R$ {:.2f}'.format(preco_final))
elif opcao == 3:
    print('Qual o número de parcelas?')
    parcelas = int(input('Digite o número de parcelas: '))
    preco_final = preco_normal * 1.20
    parcela = preco_final / parcelas
    print('O valor a ser pago é: R$ {:.2f}, em 3x de R$ {:.2f}'.format(preco_final, parcela))
else:
    print('O valor a ser pago é: R$ {:.2f}, em 2x de {:.2f}'.format(preco_normal, preco_normal / 2))
print('-' * 45)
print('Obrigado pela preferência! Volte sempre!')
print('-' * 45)
