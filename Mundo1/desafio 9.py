#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
#Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%

salario = float(input('Digite o salario do funcionário: R$ '))
sm = salario + (salario * 10 / 100)
smn = salario + (salario * 15 / 100)
if salario >1250.00:
    print('Seu novo salário, com aumento de 10% é R$:{} '.format(sm))
else:
    print('Seu novo salário com aumento de 15% é R$:{} '.format(smn))
