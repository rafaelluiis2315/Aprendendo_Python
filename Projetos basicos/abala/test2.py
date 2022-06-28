
import mysql.connector

conexao = mysql.connector.connect(
    host= '209.209.40.87',
    port=19505,
    user='admin',
    password='dVSsK94z',
    database='Projeto'
)

cursor = conexao.cursor()
def ADM():

    while True:
        print('\n','='*129,'\n')
        print(' 1 - Checar registros em uma tabela.')
        print(' 2 - Inserir um registro em tabelas.')
        print(' 3 - Atualizar uma informação em uma tabela.')
        print(' 4 - Deletar um registro de uma tabela.')
        print(' 5 - Finalizar Consultas')

        info = input(' Digite o número da função que você deseja executar: ')

        def funcao_ler(tabela_consult):
            comando = f'SELECT * FROM {tabela_consult}'
            cursor.execute(comando)
            resultado = cursor.fetchall()  # ler o banco de dados

            if tabela_consult == 'clientes':

                for registro in resultado:
                    posicao_registro = resultado.index(registro)
                    conteudo_registro = resultado[posicao_registro]

                    print(f'\n', ('='*27), f'[{posicao_registro + 1}° registro]', ('='*27))
                    print(f' CPF do cliente: {conteudo_registro[0]}')
                    print(f' Nome do cliente: {conteudo_registro[1]}' .replace("[('", "") .replace("',)]", ''))
                    print(f' Telefone: {conteudo_registro[2]}')
                    print(f' E-mail: {conteudo_registro[3]}')


            elif tabela_consult == 'fornecedores':

                for registro in resultado:
                    posicao_registro = resultado.index(registro)
                    conteudo_registro = resultado[posicao_registro]

                    print(f'\n', ('='*27), f'[{posicao_registro + 1}° registro]', ('='*27))
                    print(f' Nome: {conteudo_registro[0]}')
                    print(f' Numero do fronecedor: {conteudo_registro[1]}')
                    print(f' Tipo: {conteudo_registro[2]}')
                    print(f' E-mail: {conteudo_registro[3]}')
                    print(f' Telefone: {conteudo_registro[4]}')

            elif tabela_consult == 'produtos':

                for registro in resultado:
                    posicao_registro = resultado.index(registro)
                    conteudo_registro = resultado[posicao_registro]


                    print(f'\n', ('='*27), f'[{posicao_registro + 1}° registro]', ('='*27))
                    print(f' ID: {conteudo_registro[0]}')
                    print(f' Descrição: {conteudo_registro[1]}')
                    print(f' Preço: {conteudo_registro[2]}')
                    print(f' Codigo de barras: {conteudo_registro[3]}')
                    print(f' Data de Fabricação: {conteudo_registro[5]}')
                    print(f' Data de Validade: {conteudo_registro[6]}')
            
            elif tabela_consult == 'estoque':

                for registro in resultado:
                    posicao_registro = resultado.index(registro)
                    conteudo_registro = resultado[posicao_registro]


                    print(f'\n', ('='*27), f'[{posicao_registro + 1}° registro]', ('='*27))
                    print(f' ID: {conteudo_registro[0]}')
                    print(f' Nome lote: {conteudo_registro[1]}')
                    print(f' Quantidade: {conteudo_registro[2]}')
                    print(f' Data de entrada: {conteudo_registro[3]}')
                    print(f' Codigo lote: {conteudo_registro[4]}')


        # CREATE
        if info == "1":

            # READ
            print('\n','='*129,'\n')
            print(" TABELAS: CLIENTES, PRODUTOS, FORNECEDORES e ESTOQUE")
            tabela_consult = str(input(' Digite o nome da tabela que deseja consultar: ')).lower()

            print('\n', ('='*55), "[RESULTADO]", ('='*55), '\n')

            funcao_ler(tabela_consult)
            
        elif info == "2":

            #CREADE

            print('\n', '='*129, '\n')
            print(" TABELAS: PRODUTOS, FORNECEDORES e ESTOQUES")
            tabela_insercao = str(input(' Digite o nome da tabela que deseja cadastra: ')).lower()


            if tabela_insercao == "produtos":
                
                print('\n', ('='*55), "[DADOS NECESSÁRIOS]", ('='*55), '\n')
                # Armazena descrição do porduto
                discricao_produto = str(input(" Qual a descrição do produto? "))
                # Armazena preço unitario do porduto
                preco_unitario = float(input(" Qual o preço unitario do produto (use ponto no lugar de virgulas): "))
                # Armazena codigo de barras do porduto
                codigo_barras = int(input(" Qual o codigo de barras do produto: "))
                # Armazena numero fornecedor do porduto
                numero_fornecedor = int(input(" Qual o numero do fornecedor: "))
                # Armazena data de fabricação do porduto
                data_fabricacao = str(input(" Qual o data de fabrição do produto: "))
                # Armazena data de vencimento do porduto
                data_vencimento = str(input(" Qual a data de vencimento do produto: "))

                # insere cadostro no BD
                comando = f'INSERT INTO produtos (DESCRiÇAO_PRODUTO, PREÇO_UNITARIO, CODIGO_BARRAS, NUMERO_FORNECEDOR, DATA_FABRICAÇAO, DATA_VENCIMENTO) VALUES ("{discricao_produto}", {preco_unitario}, {codigo_barras}, {numero_fornecedor}, {data_fabricacao}, {data_vencimento})'
                cursor.execute(comando)
                conexao.commit()  # edita o banco de dados

            elif tabela_insercao == "fornecedores":

                print('\n', ('='*55), "[DADOS NECESSÁRIOS]", ('='*55), '\n')
                # nome do Armazena
                nome_fornecedor = str(input(" Qual o nome do fornecedor? "))
                # Armazena CPF
                numero_fornecedor = int(input(" Qual o numero do fornecedor: "))
                # Armazena email
                tipo_fornecedor = str(input(" Qual o tipo do fornecedor? "))
                # Armazena email
                email_fornecedor = str(input(" Qual o E-mail do fornecedor? "))
                # Armazena telefone
                telefo_fornecedor = str(input(" Qual o Telefone do fornecedor? "))

                # insere cadostro no BD
                comando = f'INSERT INTO fornecedores (NOME, CNPJ, EMAIL, TELEFONE) VALUES ("{nome_fornecedor}", "{numero_fornecedor}", "{email_fornecedor}", "{telefo_fornecedor}")'
                cursor.execute(comando)
                conexao.commit()  # edita o banco de dados

            elif tabela_insercao == "estoques":
                
                print('\n', ('='*55), "[DADOS NECESSÁRIOS]", ('='*55), '\n')
                # Armazena nome do lote
                nome_lote = str(input(" Qual o nome do lote? "))
                # Armazena quantidade
                quantidade = int(input(" Quantidade do lote : "))
                # Armazena data de entrada
                data_entrada = str(input(" Data de entrada (COLOCAR TUDO JUNTO, EX:(20220101) : "))
                # Armazena codigo do lote
                codigo_lote = int(input(" Codigo do lote: "))

                comando = f'INSERT INTO estoque (NOME_LOTE, QUANTIDADE, DATA_ENTRADA, CODIGO_LOTE) VALUES ("{nome_lote}", "{quantidade}", "{data_entrada}", "{codigo_lote}")'
                cursor.execute(comando)
                conexao.commit()

            print('\n', ('='*55), "[CADASTRO CONCLUIDO]", ('='*55), '\n')
            funcao_ler(tabela_insercao)


        elif info == "3":
            # UPDATE
            print('\n','='*129,'\n')
            print(" TABELAS: CLIENTES, PRODUTOS, FORNECEDORES e ESTOQUES")
            tabela_atualizacao = str(input('Digite o nome da tabela que deseja atualizar: ')).lower()

            print('\n', ('='*55), "[DADOS NECESSÁRIOS]", ('='*55), '\n')
            campo_alteração = input(' O campo que você deseja alterar: ')
            valor_alteração = input(' Digite o valor da alteração: ')
            campo_alteração_condição = input(' Digite o campo condicional: ')
            dado_campo_alteração_condição = input(' Digite o valor condicional do campo definido acima: ')

            comando = f'UPDATE {tabela_atualizacao} SET {campo_alteração} = {valor_alteração} WHERE {campo_alteração_condição} = "{dado_campo_alteração_condição}" ;'
            cursor.execute(comando)
            conexao.commit()  # edita o banco de dados

            print('\n', ('='*55), "[ATUALIZAÇÃO CONCLUIDO]", ('='*55), '\n')
            funcao_ler(tabela_atualizacao)

        elif info == "4":

            # DELETE
            print('\n','='*129,'\n')
            print(" TABELAS: CLIENTES, PRODUTOS, FORNECEDORES e ESTOQUES")
            tabela_delete = str(input(' Digite o nome da tabela que deseja deletar o dado: ')).lower()

            print('\n', ('='*55), "[DADOS NECESSÁRIOS]", ('='*55), '\n')
            campo_condição_delete = input(' O campo do dado que deseja deletar: ').lower()
            dado_delete = input(' Digite o dado que vai ser deletado: ')
            print('\n','='*129,'\n')

            print ("\n Tem certeza que você quer deletar um dado?")
            print (" Esse dado não podera ser recuperado depois dessa operação! \n")
            decicao = input(" SIM ou NÃO: ").lower()

            if decicao == "sim":

                comando = f'DELETE FROM {tabela_delete} WHERE {campo_condição_delete} = "{dado_delete}" ;'
                cursor.execute(comando)
                conexao.commit() # edita o banco de dados
                print('\n', ('='*27), "[DELETE CONCLUIDO]", ('='*27), '\n')
                funcao_ler(tabela_delete)

            elif decicao == "não":
                print(" OK DELETE CANCELADO")

            
        elif info == "5":
            break

        else:
            print("Digite uma opção valida")


def USER_PADRAO():
    while True:
            print('\n','='*129,'\n')
            print(' 1 - Ver produtos.')
            print(' 2 - Ver me carrinho.')
            print(' 5 - Finalizar Consultas')

            info = input(' Digite o número da função que você deseja executar: ')

            # CREATE
            if info == "1":
                def funcao_ler_user(tabela_consulta_user):
                    comando = f'SELECT * FROM {tabela_consulta_user}'
                    cursor.execute(comando)
                    resultado = cursor.fetchall()  # ler o banco de dados

                    print('\n', ('='*55), "[RESULTADO]", ('='*55), '\n')

                    for registro in resultado:
                        posicao_registro = resultado.index(registro)
                        conteudo_registro = resultado[posicao_registro]

                        print(f'\n', ('='*27), f'[{posicao_registro + 1}° registro]', ('='*27))
                        print(f' ID: {conteudo_registro[0]}')
                        print(f' Descrição: {conteudo_registro[1]}')
                        print(f' Preço: {conteudo_registro[2]}')
                        print(f' Codigo de barras: {conteudo_registro[3]}')
                        print(f' Data de Fabricação: {conteudo_registro[5]}')
                        print(f' Data de Validade: {conteudo_registro[6]}')

                funcao_ler_user('produto')

            elif info == "2":
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
                    
            elif info == "5":
                break

            else:
                print("Digite uma opção valida")

while True: 
    print('Ola Seja Bem vindo a ABALA')
    print('1 - Login')
    print('2 - Cadastrar-se')
    print('0 - Sair do site ABALA')
    home_cecisao = input('Digite a opição desejada')

    if home_cecisao == '1':

        verifica_nome = input('Coloque seu Nome: ')
        verifica_senha = input('Coloque sua senha: ')

        comando = f'SELECT * FROM clientes'
        cursor.execute(comando)
        resultado = cursor.fetchall() 

        for registro in resultado:
            posicao_registro = resultado.index(registro)
            conteudo_registro = resultado[posicao_registro]

            nome = (f'{conteudo_registro[1]}' .replace("[('", "") .replace("',)]", ''))
            senha = conteudo_registro[4]

            if verifica_nome == nome and verifica_senha == senha:
                confirmacao = 'login valido'
                break
            elif verifica_nome == "rafael luis" and verifica_senha == "bolado":
                confirmacao = 'login ADM'
            elif verifica_nome == "rafael luis" and verifica_senha == "bolado":
                confirmacao = 'login ADM'

        if confirmacao == 'login valido':
            USER_PADRAO()
        elif confirmacao == 'login ADM':
            ADM()
        else:
            print('login invalido')

    elif home_cecisao == '2':

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
    elif home_cecisao == '0':
        break
    else:
        print('Digite uma opção valida')

cursor.close()
conexao.close()