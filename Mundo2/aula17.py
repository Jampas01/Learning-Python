#Faça um programa que leia o peso de cinco pessoas. 
#No final, mostre qual foi o maior e o menor peso lidos

maior = 0
menor = 0
for n in range(1, 6):
    peso = float(input('Dígite o peso da pessoa {}ª: '.format(n)))
    if n == 1:
        maior = peso
        menor = peso
    else:
        if  peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso encontarado foi: {}.\nE o menor peso encontrado foi: {}.'.format(maior, menor))
