#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores
soma = 0
cont = 0
resposta = 'S'
maior = menor = 0

while resposta in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1

    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resposta = input('Quer continuar [S/N]: ').strip().upper()
media = soma / cont
print('Você digitou {} números;\nA média dos valores foi {};\nO maior valor digitado foi {};\nO menor valor digitado foi {};\nFIM DO PROGRAMA'.format(cont, media, maior, menor))
