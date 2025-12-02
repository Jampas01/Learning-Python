#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer
import random

print('Vou pensar em um número, será que você adivinha qual é?...')
npc = random.randint(0, 10)
acerto = False
nt = 0
while not acerto:
    tentativas = int(input('Seu Palpite: '))
    nt += 1
    if tentativas == npc:
        acerto = True
    else:
        if tentativas < npc:
                print('Mais alto!')
        elif tentativas > npc:
                print('Mais baixo!')
print('Parabéns, você acertou!\nE o número de tentativas foi de: {}'.format(nt))
