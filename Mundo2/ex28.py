#crie um programa que leia a idade e o sexo de varias pessoas, a cada pessoa cadastrada o programa devera perguntar se o usuario quer ou nao continuar no final mostre:
#A- quantas pessoas tem mais de 18 anos de idade
#B- quantos homens foram cadastrados
#C- quantas mulheres tem menos de 20 anos


maiores = homens = mulheres = total = 0     #contadores
while True:
    idade = int(input('Digite a idade: '))
    sexo = str(input('Sexo: [M]  [F]: ')).strip().upper()
    total += 1
    if idade >= 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    r = str(input('Deseja continuar a adicionar pessoas? [S] SIM   [N] NÃO: ')).strip().upper()
    if r == 'N':
        break
print('Foram adicionadas {} pessoas com mais de 18 anos; {} homens; E {} mulher(es) com menos de 20 anos.\nForam adicionadas no total, {} pessoas.'.format(maiores, homens, mulheres, total))
