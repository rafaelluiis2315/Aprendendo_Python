import mysql.connector


conexao = mysql.connector.connect(
host = '209.209.40.87',
port = 19505,
user = 'Teste',
password = '123456789',
database = 'BD_MACAW'
)

cursor = conexao.cursor()



comando = f'SELECT NOME_CURSO FROM TB_CURSO'
cursor.execute(comando)
resultado = cursor.fetchall()

cursos = []
cursos_solo = []

for curso in resultado[0:len(resultado)]:
    cursos.append(curso)
    print(''cursos)
    

for curso in cursos:
    curso_tratado = cursos[0]
    novo_curso = curso_tratado[0].replace('{}', '')
    cursos_solo.append(novo_curso)
    print(curso_tratado)
    print(novo_curso)
    print(cursos_solo)


print(cursos_solo)

cursor.close()
conexao.close()
