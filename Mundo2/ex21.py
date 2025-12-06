#faça um programa que leia o primeiro termo e a razão de uma PA, mostrando os 10 primeiroes termos usando "WHILE"  an = a1 + (n - 1) r


'''n = float(input('Digite um número: '))
r = float(input('Digite a razão: '))
c = 1
t = n
while c <= 10:
    print(t)
    t += r
    c += 1
print('fim')'''


#GUANABARA VERSION


print('Gerador de PA')
print('-=' * 8)
primeiro = int(input('Primeiro termo: '))
razao = int(input('digite a razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} → '.format(termo), end = '')
    termo += razao
    cont += 1
print('FIM')

