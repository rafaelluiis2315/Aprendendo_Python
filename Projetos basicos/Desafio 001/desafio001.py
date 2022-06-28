### DESENVOLVEDORES: RAFAEL LUÍS | IURI TORRES ###

# IMPORTAÇÕES

from ast import While

# ACESSO AO FORMULÁRIO

print('\n\n')
print('===================[ACESSO]===================\n')            # Espaçamento e Divisória

while True:
    password = input('Qual é a sua senha?: ')

    if password == 'aluno123':
        print('\nAcesso Liberado')

        break

    else:
        print('\nAcesso Negado\n')
        print('==============================================\n')


print('\n=================[FORMULÁRIO]=================\n')          # Espaçamento e Divisória

# COLETA DE DADOS PESSOAIS

nome = input('Qual o seu nome? ')                                    # Pergunta e Armazena a variável nome
print('Olá, é um prazer te conhecer {}!'. format(nome))

anoNascimento = int(input('Qual o ano do seu Nascimento? '))         # Pergunta e Armazena a variável anoNascimento
profissao = input('Qual sua profissão? ')                            # Pergunta e Armazena a variável profissao
idade = int(input('Qual sua idade? '))                               # Pergunta e Armazena a variável idade


# CÁLCULO MAIOR DE IDADE

resultadoSoma = (anoNascimento + 2022)                               # Cálculo anoNascimento + 2022 e Cálculo de maior de idade

if idade >= 18:
    maiordeidade = 'Sim'
else:
    maiordeidade = 'Não'


# IMPRESSÃO

print('\n============[SOMA ENTRE VARIÁVEIS]============\n')              # Divisória

x = int(input('Declare X: ' ))                                       # Recebe o primeiro número
y = int(input('Declare y: ' ))                                       # Recebe o segundo número

    ## CONDIÇÃO PARA ESCOLHA DE OPERADOR ##

while True:

    operador = input('Qual operação você deseja fazer (+, -, *, /): ')   # Declara o operador do cálculo

    if operador == '+':
        resultado = x + y
        
        break
    
    elif operador == '-':
        resultado = x - y

        break
    
    elif operador == '*':
        resultado = x * y

        break
    
    elif operador == '/':
        resultado = x / y
    
        break

    else:
        print('\n {}, Você não declarou um operador válido.\n'. format(nome))


#######################################
    
print('\n===============[DADOS PESSOAIS]===============\n')       # Imprime os dados pessoais
print('Nome: {}'. format(nome))
print('Idade: {}'. format(idade))
print('Profissão: {}'. format(profissao))

print('\n(Maior ou igual que 18, Sim, menor que 18, Nao)')
print('Maior de Idade: {}'. format(maiordeidade))

print('\nResultado da operação: {}'. format(resultado))
    
print('\n==============================================\n')      # Imprime os dados pessoais