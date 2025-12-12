#Crie um programa que leia o nome e o preço de vários produtos.O programa devera perguntar se o usuario vai ou nao continuar. No final mostre: A - total gasto    B - quantos produtos custam mais de 1k     C - nome do produto mais barato.


total = produtos1k = 0
nome_produto_barato = ''
primeiro = True
while True:
    nome_produto = str(input('Digite o nome do produto:\n '))
    preço_produto = float(input('Digite o valor do produto R$: '))
    total += preço_produto
    resposta = str(input('Deseja adicionar mais algum produto? [S]  [N]')).strip().upper()
    if preço_produto > 1000.00:
        produtos1k +=1
    if primeiro:
        menor_preço = preço_produto
        nome_produto_barato = nome_produto
        primeiro = False
    else:
        if preço_produto < menor_preço:
            menor_preço = preço_produto
            nome_produto_barato = nome_produto
    if resposta == 'N':
        break
print('-=' * 10)
print('O total gasto na sua compra foi de R$: {:.2f}\nProdutos com valor acima de R$: 1.000,00: {}\nE o produto mais barato foi: {}, custando R$: {}'.format(total, produtos1k, nome_produto_barato, menor_preço))
