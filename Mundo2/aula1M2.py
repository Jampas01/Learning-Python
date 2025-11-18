#AULA 1 MUNDO 2 - PYTHON

nome = str(input('Qual o seu nome? '))
if nome == 'Jampas':
    print('Vai trabalhar vagabundo!')
elif nome == 'Paulo':
    print('Que nome feio!')
elif nome == 'Maria' or nome == 'Osvaldo' or nome == 'Cabeçote':
    print('Chame o Jampinhasss!!!')
print('-=' * 200)
print('Tenha um Bom dia, {}!'.format(nome))
