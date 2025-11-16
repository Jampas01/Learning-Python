# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário 
# escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal

import math
num = int(input('Digite um número INTEIRO qualquer: '))
print('Escolha a base para a conversão: ')
print('1 - Binário')
print('2 - Octal')
print('3 - Hexadecimal')
opcao = int(input('Sua opçaõ: '))
if opcao == 1:
    print('O número {} em BINÁRIO é: {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('O número {} em OCTAL é: {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('O número {} em HEXADECIMAL é: {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida! Tente Novamente.')
    