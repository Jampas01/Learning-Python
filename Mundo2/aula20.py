#Faça um programa que leia um numero qualquer e moste o seu fatorial;ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
'''from math import factorial

n = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))'''


'''n = int(input('Digite um numero para saber seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end = '')
while c > 0:
    print('{}'.format(c), end = '')
    print(' x ' if c > 1 else ' = ', end = '')
    f *= c
    c -= 1
print('{}'.format(f))'''


n = int(input('Digite um número para saber o seu fatorial: '))
f = 1
print('Calculando {}! = '.format(n))
for c in range (n, 0, -1):
    print('{}'.format(c), end = '')
    print(' x ' if c > 1 else ' = ', end = '')
    f *= c
print('{}'.format(f))
