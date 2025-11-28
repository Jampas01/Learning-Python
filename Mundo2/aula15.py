#Crie um programa que leia uma frase qualquer e 
#diga se ela é um palíndromo, desconsiderando os espaços

frase = str(input('Digite uma frase: ')).strip().upper()
plv = frase.split()
jt = ''.join(plv)
'''ivs = '''
ivs = jt[::-1]
'''for letra in range(len(jt) -1, -1, -1):
    ivs += jt[letra]'''
print(jt, ivs)
if ivs == jt:
        print('A frase {} É UM PALÍNDROMO!'.format(frase))
else:
        print('A frase {} NÃO É UM PALÍNDROMO!'.format(frase))

print('APERTE CTRL + F5 PARA TESTAR OUTRA PALAVRA!')
