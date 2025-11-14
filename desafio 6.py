#Desenvolva um programa que pergunte a distância de uma viagem em Km. 
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

viagem = float(input('Digite quantos KMs tem a viagem: '))
pvc = 0.50
pvl = 0.45
vc = viagem * pvc
vl = viagem * pvl
if viagem > 200:
    print('O valor do KM para essa viagem é de R$: {} \nA passagem custará R$: {:.2f}'.format(pvl, vl))
else:
    print('O valor do KM para essa viagem é de R$: {} \nA passagem custará R$: {:.2f}'.format(pvc, vc))
print('-=-' * 6, 'BOA VIAGEM!!!!', '-=-' * 6)
