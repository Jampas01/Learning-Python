#Crie um programa que leia o ano de nascimento de sete pessoas. 
#No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
atual = date.today().year
tmaior = 0
tmenor = 0
for pess in range(1, 8):
    nsc = int(input('Digite o ano em que a {}ª pessoa nasceu: '.format(pess)))
    idade = atual - nsc
    if idade >= 21:
        tmaior += 1
    else:
        tmenor += 1
print('O número de pessoas maiores de idade é {}'.format(tmaior))
print('O número de pessoas menores de idade é {}'.format(tmenor))
    