#Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso de zero até vinte. Seu programa devera ler o numero pelo teclado (entre 0 e 20) e mostrá-lo por extenso.


resposta = 'S'
while resposta == 'S':
    indice = int(input('Digite, um numero de 0 à 20 para vê-lo por extenso: '))
    lista = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

    if indice > 20 or indice < 0:
        print('Número inválido. Digite um nùmero de 0 à 20.')
    else:
        print(lista[indice])
        resposta = input('Deseja continuar? [S/N]') .strip() .upper()
    if resposta == 'N':
        break


#Guanabara version
#cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', #'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

#while True:
#   num = int(input('digite um numero entre 0 e 20: '))
#   if 0 <= num <=20:
#    break
#   print('tente novamente!')
#print(f'Você digitou o numero {cont[num]}')
