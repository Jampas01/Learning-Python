#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

#EQUILÁTERO: todos os lados iguais

#ISÓSCELES: dois lados iguais, um diferente

#ESCALENO: todos os lados diferentes


print('=-' * 20)
print('ANALISADOR DE TRIÂNGULOS')
print('=-' * 20)
s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
#verifica se pode formar triangulo
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos {}, {} e {} PODEM FORMAR um triângulo!'.format(s1, s2, s3))
#verifica tipo de triangulo
    if s1 == s2 == s3:
        print('O tipo do triângulo formado é: EQUILÁTERO!')
    elif s1 != s2 != s3 != s1:
        print('O tipo de triângulo formado é: ESCALENO!')
    else:
        print('O tipo de triângulo formado é: ISÓSCELES!')
else:
    print('Os segmentos {}, {} e {} NÃO PODEM FORMAR um triângulo!'.format(s1, s2, s3))
