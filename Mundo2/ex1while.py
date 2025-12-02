#Faça um programa que leia o sexo de uma pessoa
# mas só aceite os valores ‘M’ ou ‘F’. 
#Caso esteja errado, peça a digitação novamente até ter um valor correto.

r = ''
while r != 'F' and r != 'M':
    r = input('Informe seu sexo [M/F]:').strip().upper()
    print('Opção inválida, informe uma opção valida por favor!')
print('Obrigado, você digitou o sexo: {}'.format(r))
print ('fim')
