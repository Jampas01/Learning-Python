#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida

# < 7.0 = reprovado
# > 7.0 = aprovado

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media > 7.0:
    print('Sua média foi {:.1f} e você está APROVADO!'.format(media))
    print('PARABÉSNS!!!')
elif 6.0 <= media <= 7.0:
    print('Sua média foi {:.1f} e você está de recuperação!'.format(media))
    print('Estude mais na próxima!')
else:
    print('Sua média foi {:.1f} e você está REPROVADO!'.format(media))
    print('Se esforce mais na próxima!')
print('-=' * 3, 'BOAS FÉRIAS', '-=' * 3)
