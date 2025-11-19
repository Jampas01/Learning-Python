#mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num = int(input('Digite um número para ver sua tabuada: '))
print('-=' * 5, 'A tabuada de {} é:'.format(num), '-=' * 5)
for c in range (1, 11):
    print('{} x {} = {}'.format(num, c, num * c))
print('==' * 20)
