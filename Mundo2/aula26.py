#Faça um programa que jogue par ou impar com o computador. o jogo so sera interrompido quando o usuario perder, mostrando o total de vitorias consecutivas.

import random
cont = 0

print('-=' * 15)
print('VAMOS JOGAR ÍMPAR OU PAR?')
print('-=' * 15)
while True:
    ip = str(input('Ímpar [I] ou par [P]?: ')).strip().upper()
    nj = int(input('Digite um número de 1 a 10: '))
    npc = random.randint (1, 10)
    total = npc + nj

    r = 'P' if total % 2 == 0 else 'I'
    if ip == 'I':
        pj = 'I'
        ppc = 'P'
    else:
        pj = 'P'
        ppc = 'I'
    print('Você jogou {}, e o computador {}. Total = {}, deu {}'.format(ip, npc, total, r))
    if pj == r:
        print('Você venceu!')
        cont += 1
    else:
        print('Você perdeu!')
        break
print('Fim de jogo! Você venceu {}vez(es) seguidas!'.format(cont))
