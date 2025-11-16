#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR
numero = int(input('Digite um número para saber se ele é PAR ou Ímpar: '))
n = numero % 2
if n == 1:
    print('o numero {} é Ímpar'.format(numero))
else:
    print('O numero {} é par'.format(numero))
    
