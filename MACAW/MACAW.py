from typing import Type
from PySimpleGUI import PySimpleGUI as sg
import mysql.connector

conexao = mysql.connector.connect(
    host = '209.209.40.87',
    port = 19505,
    user = 'Teste',
    password = '123456789',
    database = 'BD_MACAW'
)

cursor = conexao.cursor()


#Layout

def janela_login():
    sg.theme('Reddit')
    layout = [
        [sg.Image(r"C:\Users\rafae\OneDrive\Área de Trabalho\MACAW\Logo_200.png", background_color= 'SpringGreen', s = (None,None), pad = (150, None))],
        [sg.Text('                Usuario:', background_color= 'SpringGreen'), sg.Input(key='usuario', size = (30, 1))],
        [sg.Text('                Senha:  ', background_color= 'SpringGreen'), sg.Input(key='senha', password_char='*', size = (30, 1))],
        [sg.Checkbox('Salvar o login', background_color= 'SpringGreen', pad = (110, 10))],
        [sg.Button('Entrar', pad = (200, 0))]
    ]

    return  sg.Window('Tela de Login', layout,icon=r'Logo_200.ico',  background_color= 'SpringGreen', size = (500, 600), finalize= True )


def janela_Home():
    layout2 =[
        [sg.Image(r"C:\Users\rafae\OneDrive\Área de Trabalho\MACAW\Logo_200.png", background_color= 'SpringGreen', s = (None,None), pad = (150, None))],
        [sg.Text('Nome:', background_color= 'SpringGreen'), sg.Input(key='nome', size = (30, 1), p = (19,(0,0)))],
        [sg.Text('Email:', background_color= 'SpringGreen'), sg.Input(key='email', size = (30, 1), p = (19,(0,0)))],
        [sg.Text('Telefone:', background_color= 'SpringGreen'), sg.Input(key='telefone', size = (30, 1))],
        [sg.Text('CEP:', background_color= 'SpringGreen'), sg.Input(key='cep', size = (30,1), p = (25,(0,0)))],
        [sg.Text('CPF:', background_color= 'SpringGreen'), sg.Input(key='cpf', size = (30, 1), p = (25,(0,0)))],
        [sg.Button('Enviar', pad = (200,(10,0)))]
    ]

    return sg.Window('Tela de Login', layout2, background_color= 'SpringGreen', size = (500, 600), finalize= True)


#Janela
janela1, janela2 = janela_login(), None

#Ler os eventos 
while True:
    window, eventos, valores = sg.read_all_windows()
    #Quando a janela for fechada
    if window == janela1 and eventos == sg.WIN_CLOSED:
        break   
    #Quando ir pra outra janela
    if eventos == 'Entrar':

        verificacao = "SELECT EMAIL FROM TB_FUNCIONARIOS WHERE EMAIL ='{}'".format(valores['usuario'])
        cursor.execute(verificacao)
        resultado = cursor.fetchall()

        if len(resultado) != 0:
            verificacao_campo_funcionarios = 'EMAIL'

        verificacao = "SELECT CPF FROM TB_FUNCIONARIOS WHERE CPF ='{}'".format(valores['usuario'])
        cursor.execute(verificacao)
        resultado = cursor.fetchall()

        if len(resultado) != 0:
            verificacao_campo_funcionarios = 'CPF'
        else:
            verificacao_campo_funcionarios = 'INVALIDO'



        if verificacao_campo_funcionarios == 'EMAIL' or verificacao_campo_funcionarios == 'CPF':

            verificacao = "SELECT SENHA FROM TB_FUNCIONARIOS WHERE {} ='{}'".format(verificacao_campo_funcionarios, valores['usuario'])
            cursor.execute(verificacao)
            password_login = cursor.fetchall()

            
            if valores['senha'] in password_login[0]:

                janela2 = janela_Home()
                janela1.hide()
            
        elif verificacao_campo_funcionarios == 'INVALIDO':
            sg.popup('Você digitou um usuario ou senha inválido, tente novamente.')

    if eventos == 'Enviar':

        nome= str(valores['nome']).upper()
        email = str(valores['email'])
        telefone = str(valores['telefone'])
        cep = str(valores['cep'])
        cpf = str(valores['cpf'])

        # insere cadostro no BD
        comando = f'INSERT INTO TB_ALUNO (NOME_ALUNO, EMAIL, TELEFONE, CEP, CPF) VALUES ("{nome}", "{email}", "{telefone}", "{cep}", "{cpf}")'
        cursor.execute(comando)
        conexao.commit()  # edita o banco de dados

        sg.popup('Cadastro realizado com sucesso!!')

    if window == janela2 and eventos == sg.WIN_CLOSED:
        break 


cursor.close()
conexao.close()