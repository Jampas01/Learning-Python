#CRIE UM PROGRAMA QUE LEIA DOIS VALORES E MOSTRE UM MENU NA TELA:
#[1] - SOMAR; [2] - MULTIPLICAR; [3] - MAIOR; [4] - NOVOS NÚMEROS; [5] - SAIR;

n1 = float(input('digite um número: '))
n2 = float(input('digite outro númro: '))
usuario = 0

while usuario != 5:
    print('escolha a opção desejada:\n')
    print('[1] - SOMAR')
    print('[2] - MULTIPLICAR')
    print('[3] - MAIOR')
    print('[4] - NOVOS NUMEROS')
    print('[5] - SAIR')
    usuario = int(input('Sua opção: '))
    if usuario == 1:
       print('A soma dos valores {} e {} é igual a {}'.format(n1, n2, n1 + n2))
    elif usuario == 2:
        print('A multiplicação dos valores {} e {} é igual a {}'.format(n1, n2, n1 * n2))
    elif usuario == 3:
        if n1 > n2:
            print('o maior número é {}'.format(n1))
        elif n2 > n1:
            print(' o maior numero é {}'.format(n2))
        else:
            print('não ha numero maior; os dois valores são iguais')
    elif usuario == 4:
        print('digite novos valores: ')
        n1 = float(input('primeiro numero: '))
        n2 = float(input('segundo numero: '))
    elif usuario == 5:
        print('saindo do programa...')
    else:
        print('opcão inválida, digite um numero de 1 ate 5 por favor!!')
print('FIM')
