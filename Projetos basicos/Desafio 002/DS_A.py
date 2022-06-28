### DESENVOLVEDOR : RAFAEL LUÍS | IURI TORRES ###

### IMPORTAÇÕES ###

from numpy import float64
import pandas as pd
import openpyxl
import os

# LISTAS

lista_meses = ['janeiro', 'fevereiro', 'março']

# VARIÁVEIS GERAIS

preco_residencial = 0.3
preco_comercial = 0.5
preco_industrial = 0.7

consulta_de_clientes = 'CONSULTA DE CLIENTES'

### SISTEMA DE CONSULTA DE CONSUMIDORES ###

# LEITURA E FORMATAÇÃO DOS DADOS DAS PLANILHAS

for mes in lista_meses:

    tabela_consumidores = pd.read_excel(f'C:\\Users\\rafae\\OneDrive\\Área de Trabalho\\Python\\Desafio 002\\{mes}.xlsx') ##Tem que mudar o caminho para chamar as planilhas

    tabela_consumidores['ID'] = tabela_consumidores['ID'].apply(lambda x: str(x).replace(',','.'))
    tabela_consumidores['ID'] = tabela_consumidores['ID'].astype('float64')

# SELEÇÃO DE MÊS, ID E CÁLCULOS

os.system('cls')

print('\n','='*57,'\n')   # DIVISÓRIA

print(consulta_de_clientes.center(57))

while True:

        # ENTRADA DE DADOS

    print('\n','='*57,'\n')   # DIVISÓRIA

    print(' Digite 0 nos 2 campos para parar a consulta!\n')

    consulta_mes = input(' Qual mês você deseja acessar?: ')
    ID_consumidor = int(input(' Digite o ID do Consumidor que deseja consultar: '))

        # PROCURA OS DADOS REFERENTES DO ID NA PLANILHA E ARMAZINA EM VARIÁVEIS RESPECTIVAS

    if consulta_mes in lista_meses and ID_consumidor in tabela_consumidores['ID']:

        mes = (f'{consulta_mes}')
        tabela_consumidores = pd.read_excel(f'C:\\Users\\rafae\\OneDrive\\Área de Trabalho\\Python\\Desafio 002\\{mes}.xlsx') ##Tem que mudar o caminho para chamar as planilhas

        nome_consumidor = tabela_consumidores.loc[ID_consumidor == tabela_consumidores['ID'], 'Consumidor'].values[0]
        tipo_consumidor = tabela_consumidores.loc[ID_consumidor == tabela_consumidores['ID'], 'Tipo'].values[0]
        consumo_consumidor = tabela_consumidores.loc[ID_consumidor == tabela_consumidores['ID'], 'KWh'].values[0]

        # CALCULA OS VALORES A SE PAGAR POR kWh

        if tipo_consumidor == 'Residencial':
            valor_do_consumo = consumo_consumidor * preco_residencial
        elif tipo_consumidor == 'Comercial':
            valor_do_consumo = consumo_consumidor * preco_comercial
        elif tipo_consumidor == 'Industrial':
            valor_do_consumo = consumo_consumidor * preco_industrial

        float(valor_do_consumo)                                                   # DEFINE VALOR COMO UMA VAR FLOAT

        soma_total_3tipos = ((consumo_consumidor * preco_residencial) + (consumo_consumidor * preco_comercial) + (consumo_consumidor * preco_industrial))
        media_tipo1e2 = ((consumo_consumidor * preco_residencial) + (consumo_consumidor * preco_comercial))/2

        # IMPRIME OS DADOS PESQUISADOS

        os.system('cls')

        print('\n','='*57,'\n')   # DIVISÓRIA

        print(consulta_de_clientes.center(57))


        print('\n\n ==================[DADOS DO CONSUMIDOR]==================\n')   # DIVISÓRIA
        print(f' ID.......................: #{ID_consumidor}')
        print(f' NOME.....................: {nome_consumidor}')
        print(f' TIPO.....................: {tipo_consumidor}')
        print(f' kWh CONSUMIDO............: {consumo_consumidor}')
        print(f' VALOR A SE PAGAR.........: R${valor_do_consumo:,.2f}')
        print(f' CONSUMO PARA OS 3 TIPOS..: R${soma_total_3tipos:,.2f}')
        print(f' MÉDIA DO CONSUMO 1 E 2...: {media_tipo1e2}')

    elif consulta_mes or ID_consumidor == '0':

        break

    else:

        os.system('cls')

        print('\n','='*57,'\n')   # DIVISÓRIA

        print(consulta_de_clientes.center(57))

        print('\n','='*57,'\n')   # DIVISÓRIA
        print(' Você digitou um mês ou um ID inválido, tente novamente!')