#jokenpo


import random
itens = ('pedra', 'papel', 'tesoura')
computador = random.randint(0, 2)
print('-=' * 5, 'JO KEN PO', '-=' * 5)
print('[0] PEDRA\n[1] PAPEL\n[2] TESOURA')
jogador = int(input('Qual é a sua jogada? '))
#jogador escolheu PEDRA
if jogador == 0 and computador == 1:
    print('computador jogou PAPEL\njogador jogou PEDRA\nCOMPUTADOR VENCE!!\n TENTE NOVAMENTE!!')
elif jogador == 0 and computador == 2:
    print('computador jogou TESOURA\njogador jogou PEDRA\nJOGADOR VENCE!!')
#jogador escolheu PAPEL
elif jogador == 1 and computador == 0:
    print('computador jogou PEDRA\njogador jogou PAPEL\njogador VENCE!!')
elif jogador == 1 and computador == 2:
    print('computador jogou TESOURA\njogador jogou PAPEL\nCOMPUTADOR VENCE!!\nTENTE NOVAMENTE!!')
#jogador escolheu TESOURA
elif jogador == 2 and computador == 0:
    print('computador jogou PEDRA\njogador jogou TESOURA\nCOMPUTADOR VENCE!!\nTENTE NOVAMENTE!!')
elif jogador == 2 and computador == 1:
    print('computador jogou PAPEL\njogador jogou TESOURA\nJOGADOR VENCE!!')
#empate
elif jogador == computador:
    print('computador jogou {}\njogador jogou {}\nEMPATE!!'.format(itens[computador], itens [jogador]))
