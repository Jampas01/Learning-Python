#EX71

#FAÇA UM PROGRAMA QUE MOSTRE A TABUADA DE VARIOS NUMEROS, UM DE CADA VEZ, PARA CADA VALOR DIGITADO PELO USUARIO. O PROGRAMA SERA INTERROMPIDO QUANDO O NUMERO SOLICITADO FOR NEGATIVO.
print('Gerador de Tabuadas...')
print('-=' * 20)

while True:
    nt = int(input('Digite um numero para saber sua tabuada (digite um numero negativo para parar): '))
    if nt < 0:
        print('Número inválido digitado.')
        break
    print('-=' * 20)
    for x in range (1, 11):
        print('{} x {} = {}'.format(nt, x, nt * x))
    print('A tabuada está pronta, obrigado por esperar!')
