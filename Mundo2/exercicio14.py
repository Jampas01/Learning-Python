#Desenvolva um programa que leia seis números inteiros e mostre a soma 
#apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o

soma = 0
pares = 0
for c in range(1, 7):
    n = int(input('Digite o {}º número: '.format(c)))
    if n % 2 == 0:
        soma += n
        pares += 1
if pares == 0:
    print('Não foi informado nenhum número par.')
else:
    print('Você informou {} números PARES e a soma entre eles é: {}'.format(pares, soma))
