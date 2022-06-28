from sre_parse import expand_template
from dataclasses import replace
from typing import Type
from unittest import result
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


def janela_Home():
    sg.theme('DarkGreen5')
   
    comando = f'SELECT NOME_CURSO FROM TB_CURSO'
    cursor.execute(comando)
    resultado = cursor.fetchall()

    cursos = []
    cursos_solo = []

    for curso in resultado[0:len(resultado)]:
        cursos.append(curso)

    for curso in cursos:
        index_curso = cursos.index(curso)
        curso_tratado = cursos[index_curso]
        novo_curso = curso_tratado[0].replace('{}', '')
        cursos_solo.append(novo_curso)
        
        
    layout2 =[

        [sg.Text('Nome:'), sg.Input(right_click_menu = cursos,key='nome', size = (30, 1), p = (19,(0,0)))],
        [sg.Text('Email:'), sg.Input(key='email', size = (30, 1), p = (19,(0,0)))],
        [sg.Text('Telefone:'), sg.Input(key='telefone', size = (30, 1))],
        [sg.Text('CEP:'), sg.Input(key='cep', size = (30,1), p = (25,(0,0)))],
        [sg.Text('CPF:'), sg.Input(key='cpf', size = (30, 1), p = (25,(0,0)))],
        [sg.Text('cursos:'), sg.Combo(values= list(cursos_solo), key = 'cursos')],
        [sg.Button('Enviar', pad = (200,(10,0)))]
    ]

    return sg.Window('Tela de Login', layout2, size = (500, 600), finalize= True)

#Janela

janela2 = janela_Home(), None

#Ler os eventos
while True:
    window, eventos, valores = sg.read_all_windows()

    #Quando a janela for fechada
    if eventos == sg.WIN_CLOSED:
        break   
    
    #Quando ir pra outra janela

    janela_Home()



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