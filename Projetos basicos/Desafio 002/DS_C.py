### DESENVOLVEDOR : RAFAEL LUÍS | IURI TORRES ###

# IMPORTAÇÕES

from ast import While
from operator import index
import os
from time import sleep
import datetime
from turtle import title

# VARIÁVEIS GERAIS

data_atual = datetime.date.today()

dia = f'{data_atual.day:0>2}'
mes = f'{data_atual.month:0>2}'
ano = f'{data_atual.year:<4}'

# LISTAS E TUPLAS

lista_produtos = ('Maçã', 2,
                  'Banana', 1,
                  'Melancia', 8,
                  'Abóbora', 10,
                  'Batata', 3,
                  'Cebola', 1.50,
                  'Alface', 0.60,
                  'Tomate', 0.75,
                  'Cenoura', 1.25)

lista_carrinho = []
lista_valortotal_carrinho = []

# PRODUTOS DA LOJA - IMPRESSAO

print('\n====================[NOSSOS PRODUTOS]====================\n')       # Imprime os dados pessoais

for posicao in range(0, len(lista_produtos)):
    if posicao % 2 == 0:
        print(f'{lista_produtos[posicao]:.<30}', end='')

    else:
        print(f'R${lista_produtos[posicao]:>6.2f}')

### SISTEMA CARRINHO ###

# SISTEMA DE ADIÇÃO DE PRODUTOS

while True:

    print('\n=========================================================\n')   # DIVISÓRIA

    produto = input('Insira um produto: ')                         # Armazena uma informação

    if produto == '0':                                             # Se digitar 0 fecha o carrinho

        break

    elif produto in lista_produtos:
        lista_carrinho.append(produto)

        os.system('cls')

        print('\n====================[NOSSOS PRODUTOS]====================\n')       # Imprime os dados pessoais

        for posicao in range(0, len(lista_produtos)):
            if posicao % 2 == 0:
                print(f'{lista_produtos[posicao]:.<30}', end='')

            else:
                print(f'R${lista_produtos[posicao]:>6.2f}')

        print('\n=========================================================\n')       # DIVISÓRIA

        print('\nCarrinho: {}\n'.format(lista_carrinho))
        print('\n{} foi adicionado ao carrinho!\nEscolha outro produto ou digite "0" para fechar o carrinho. \n'.format(produto))

    else:

        os.system('cls')

        print('\n====================[NOSSOS PRODUTOS]====================\n')       # Imprime os dados pessoais

        for posicao in range(0, len(lista_produtos)):
            if posicao % 2 == 0:
                print(f'{lista_produtos[posicao]:.<30}', end='')

            else:
                print(f'R${lista_produtos[posicao]:>6.2f}')

        print('\n=========================================================\n')       # DIVISÓRIA

        print('\nCarrinho: {}\n'.format(lista_carrinho))
        print('Ei!, não temos {} em nossa loja, verifique nossos produtos na tabela a cima!\n' .format(produto))

os.system('cls')


# TIMER PARA FINALIZAÇÃO DO PEDIDO

timer_fechamento_carrinho = [3, 2, 1]

for segundo_timer_carrinho in timer_fechamento_carrinho:
    print('\n=========================================================\n', '\nCarrinho Fechado!! \n', '\nPróxima etapa em {} segundos\n' .format(segundo_timer_carrinho), '\n=========================================================\n')       # DIVISÓRIA

    sleep(1)
    os.system('cls')

sleep(0.3)                                                         # Espera 0.3 segundos para limpar a tela
os.system('cls')                                                   # Limpa a tela

# INFORMAÇÕES - CARRINHO FECHADO

print('============ PRODUTOS NO CARRINHO: =============\n')

for produto in lista_carrinho:
    print(f'{produto:.<30}', end='')

    preco_carrinho = (lista_produtos.index(produto) + 1)                # Acha o preço do produto na tufla
    print(f'R${lista_produtos[preco_carrinho]:>6.2f}')                  # Imprime o preço no carrinho
    lista_valortotal_carrinho.append(lista_produtos[preco_carrinho])    # Adiciona o preço na lista do carrinho

print('\n================= INFORMAÇÕES: =================\n')

print('Número do pedido: #001')
print('Data do pedido: {}/{}/{}' .format(dia, mes, ano), '\n')    # Mostra a data

valor_total_carrinho = sum(lista_valortotal_carrinho)             # Soma os preços do carrinho

print('Quantidade de Itens: {}' .format(len(lista_carrinho)) )    # Conta quantos itens tem no carrinho
print(f'Valor Total: R${valor_total_carrinho:6.2f}')

print('\n================================================\n')