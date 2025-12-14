#crie umprograma que simule o funcionamento de um caixa eletrônico.No inicio pergunte ao usuario qual sera o valor sacado (numero inteiro) e o programa irá informar quantas cédulasde cada valor serão entregues. O caixa possui cédulas de R$50, R$20, R$10 e R$1.

'''cinquentao = 50
vintao = 20
deizao = 10
realzin = 1
while True:
    print('-=' * 6)
    print('Jampas bank')
    print('-=' * 6)
    saque = int(input('Digite o valor do saque: R$: '))
    if saque == 0:
        print('Encerrando o caixa eletronico...')
        break
    if saque < 0:
        print('Valor inválido!')
        continue
    cincox10 = saque // cinquentao
    resto = saque % cinquentao

    duasx10 = resto // vintao
    resto = resto % vintao

    umax10 = resto // deizao
    resto = resto % deizao

    real = resto // realzin
    resto = resto % realzin

    print('O valor solicitado sera entregue em: \n{} Cédulas de R$: 50.00\n{} Cédulas de R$: 20.00\n{} Cédulas de R$: 10.00\n{}Cédulas de R$: 1.00'.format(cincox10, duasx10, umax10, real))
    print('Jampas bank agradece a preferência! Volte sempre!')'''


#GUANABARA VERSION

print('-=' * 6)
print('{:^6}'.format('Jampas Banks'))
print('-=' * 6)
saque = int(input('Digite o valor que deseja sacar: R$ '))
total = saque
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('-=' * 15)
print('Jampas banks agradece a preferência! Volte sempre!')
