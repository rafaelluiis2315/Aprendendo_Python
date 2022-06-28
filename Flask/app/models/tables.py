import mysql.connector

conexao = mysql.connector.connect(
    host= '209.209.40.87',
    port=19505,
    user='Teste',
    password='123456789',
    database='Teste2'
)

cursor = conexao.cursor()


print('\n', '='*129, '\n')
print(" TABELAS: CLIENTES, PRODUTOS, FORNECEDORES e ESTOQUES")
tabela_insercao = str(input(' Digite o nome da tabela que deseja cadastra: ')).lower()


print('\n', ('='*55), "[DADOS NECESSÁRIOS]", ('='*55), '\n')
# Armazena nome do cliente
nome_clie = str(input(" Qual o seu nome? "))
# Armazena CPF do cliente
cpf_clie = str(input(" Qual a sua CPF ? (NÃO incluir pontos ( . ) e traços ( - )): "))
# Armazena email do cliente
email_clie = str(input(" Qual o seu E-mail? "))
# Armazena telefone do cliente
telefo_clie = str(input(" Qual o seu Telefone? "))
# Armazena senha do cliente
senha_clie = str(input(" Crie uma senha: "))

# insere cadostro no BD
comando = f'INSERT INTO clientes (cpf_cliente, nome_cliente, telefone, email, senha) VALUES ("{cpf_clie}", "{nome_clie}", "{telefo_clie}", "{email_clie}", "{senha_clie}")'
cursor.execute(comando)
conexao.commit()  # edita o banco de dados