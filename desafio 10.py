#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo


print('-=-' *20)
print('Analisador de triangulos:')
print('-=-' * 20)
s1 = float(input('primeiro segmento: '))
s2 = float(input('segundo segmento: '))
s3 = float(input('terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos {}, {} e {} PODEM FORMAR um triângulo!'.format(s1, s2, s3))
else:
    print('Os segmentos {}, {} e {} NÃO PODEM FORMAR um triângulo!'.format(s1, s2, s3))
    