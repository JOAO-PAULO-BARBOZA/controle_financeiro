import sqlite3

def criar_db(caminho_dado_csv, tabela):
    
    """Cria um banco de dados sqlite3 através de um arquivo .csv"""
    
    df = pd.read_csv(caminho_dado_csv)

    conexao = sqlite3.connect('my_db.db')

    df.to_sql(tabela, conexao, if_exists='replace', index=False)
    
    conexao.close()
    
    print('Banco de dados criado com sucesso!')


def mostrar_banco(banco_de_dados):

    """Mostra o contúdo do banco de dados"""
    
    # Crie uma conexão com o banco de dados SQLite
    conexao = sqlite3.connect(banco_de_dados)

    # Crie um cursor para executar comandos SQL
    cursor = conexao.cursor()

    # Execute um comando SQL para selecionar todos os dados da tabela "clientes"
    cursor.execute("SELECT * FROM dados")

    # Recupere os resultados da consulta
    resultados = cursor.fetchall()

    # Imprima os resultados
    for linha in resultados:
        print(linha)
    
    # Feche o cursor e a conexão com o banco de dados
    cursor.close()
    conexao.close()


def pegar_colunas(banco_de_dados):
    
    """Pega as colunas do banco de dados devolvendo uma tupla"""

    # Crie uma conexão com o banco de dados SQLite
    conexao = sqlite3.connect(banco_de_dados)

    # Crie um cursor para executar comandos SQL
    cursor = conexao.cursor()

    # Execute um comando SQL para ver as colunas da tabela "clientes"
    pegar_col = "SELECT * FROM sqlite_master WHERE type='table' AND name='dados'"
    cursor.execute(pegar_col)

    # Recupere o resultado da consulta
    tabela_info = cursor.fetchone()

    # Recupere o nome das colunas da tabela "clientes" do resultado da consulta
    colunas = [coluna_info[1] for coluna_info in cursor.execute("PRAGMA table_info(dados)").fetchall()]
    
    colunas.pop(0)
    colunas.pop(0)

    # Feche o cursor e a conexão com o banco de dados
    cursor.close()
    conexao.close()
    
    return tuple(colunas)


def inserir_dados(banco_de_dados):

    """Faz a inserção de dados no bando de dados """

    conexao = sqlite3.connect(banco_de_dados)

    cursor = conexao.cursor()
    
    colunas = pegar_colunas(banco_de_dados)
    
    valores = (tuple(len(colunas)*'?'.split()))

    # Execute um comando SQL para inserir um novo registro na tabela.
    
    resposta = 's'    
    
    while resposta == 's':      
        
        parametros = []
        
        for col in colunas:
    
            parametros.append(input(f'Insira a(o) {col} :'))

        parametros = tuple(parametros)


        comando_sql = f"INSERT INTO dados {colunas} VALUES {parametros}"
        
        cursor.execute(comando_sql)

        # Salve as alterações no banco de dados
        conexao.commit()

        resposta = input("Deseja continuar inserindo dados s/n? ")
    
    # Feche o cursor e a conexão com o banco de dados
    cursor.close()
    conexao.close()

def deletar_dados(banco_de_dados):


    """Deleta todos os dados do banco de dados"""
    
    # Crie uma conexão com o banco de dados SQLite
    conexao = sqlite3.connect(banco_de_dados)

    # Crie um cursor para executar comandos SQL
    cursor = conexao.cursor()

    # Execute um comando SQL para deletar todos os dados da tabela "dados"
    cursor.execute("DELETE FROM dados")
    
    conexao.commit()
    # Feche o cursor e a conexão com o banco de dados
    
    cursor.close()
    conexao.close()

 
















