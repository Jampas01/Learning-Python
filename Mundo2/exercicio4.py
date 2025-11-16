#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade
#se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
an = int(input('Digite o ano de nascimento: '))
sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()
#descobrindo o sexo
if sexo == 'F':
    print('O alistamento militar é obrigatório somente para homens.')
    exit()
#calculo idade
atual = date.today().year
idade = atual - an
print('Quem nasceu em {} tem {} anos em {}.'.format(an, idade, atual))
#menor de idade
if idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
    print('Seu alistamento será em {}.'.format(ano))
#no ponto de se alistar
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
#passou do ponto de se alistar
else:
    saldo = idade - 18
    ano = atual - saldo
    print('Você deveria ter se alistado há {} anos.\nNo ano de {}'.format(saldo, ano))
