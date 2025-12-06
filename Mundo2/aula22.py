#DEIXE O USUARIO ESCOLHER QUANTOS TERMOS EXIBIR:


'''print('Gerador de PA...')
print('-=-' * 7)
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
ntermos = int(input('Quantos termos dessa PA você deseja exibir? '))
termo = primeiro
c = 1
while c <= ntermos:
    print('{} → '.format(termo), end = '')
    termo += razao
    c += 1
print('FIM')'''



#GUANABARA VERSION


print('Gerador de PA...')
print('-=-' * 8)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
c = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while c <= total:
        print('{} →'.format(termo), end = '')
        termo += razao
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos voce quer mostrar a mais?'))
print('Progressão finalizada com {} termos mostrados.'.format(total))
