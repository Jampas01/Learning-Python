#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)
soma = 0
cont = 0

numeros = int(input('Digite um número (999 para parar): '))

while numeros != 999:
    soma += numeros
    cont += 1
    numeros = int(input('Digite um número (999 para parar): '))
print('O total de números digitados foi: {}, e a soma entre eles foi de: {}'.format(cont, soma))
print('FIM DO PROGRAMA')
