#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma 
#mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.


velocidade = int(input('Qual a velocidade do veiculo?: '))
multa = velocidade - 80
if velocidade > 80:
    print('Você ultrapassou o limite da via em {} KMs/H! o valor da multa será R$: {:.2f}'.format(multa, multa * 7))
    print('Tenha mais cuidado no trânsito, Dirija devagar!')
else:
    print('-=-' * 5, 'Boa Viagem!', '-=-' * 5)
    print('-=-' * 2, 'Parabéns pela boa conduta!', '-=-' * 2)
    