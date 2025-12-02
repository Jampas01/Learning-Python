#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
#No final do programa, mostre: a média de idade do grupo, qual é o 
#nome do homem mais velho e quantas mulheres têm menos de 20 anos.


soma = 0
media = 0
maiorh = 0
nomevelho = ''
menos20 = 0

for n in range (1, 5):
    print('-----{}ª pessoa-----'.format(n))
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]: ')).strip()
    soma += idade
    if n == 1 and sexo in 'Mm':
        maiorh = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maiorh:
        maiorh = idade
        nomevelho = nome
    if sexo in 'fF' and idade < 20:
        menos20 += 1

        
media = soma / 4
print('A média de idade do grupo é: {}'.format(media))
print('O homem mais velho encontrado foi: {}, e tem {} anos'.format(nomevelho, maiorh))
print('E a quantidade de mulheres com menos de 20 anos foi de: {}'.format(menos20))
