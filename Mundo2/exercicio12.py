#Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500


s = 0
ct = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        ct += 1
print('A soma de todos os números múltiplos de 3, entre 1 e 500 é {}'.format(s))
print('E a qauntidade de números múltiplos de 3 é {}'.format(ct))
