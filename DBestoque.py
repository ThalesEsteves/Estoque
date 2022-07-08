import mysql.connector
from Produtos import *

class DBestoq:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='q1w2e3',
            database='db_estoque'
        )
        self.meu_cursor = self.conexao.cursor()

    def cadastrar_fabricante(self, cod, nome):
        obg_fabricante = Fabri(cod, nome)
        comando_sql = f'insert into Fabricante' \
                      f'(nome)' \
                      f'value' \
                      f'("{obg_fabricante.nome}")'
        self.meu_cursor.execute(comando_sql)
        self.conexao.commit()

    def cadastrar_produto(self, cod, descricao, id_fabricante, quantidade):
        obg_produto = Prod(cod, descricao, id_fabricante, quantidade)
        comando_sql = f'insert into Produtos' \
                      f'(descricao, id_fabricante, quantidade)' \
                      f'value' \
                      f'("{obg_produto.descricao}",{obg_produto.id_fabricante},"{obg_produto.quantidade}")'
        self.meu_cursor.execute(comando_sql)
        self.conexao.commit()

    def listar_produto(self, cod):
        comando_sql = f'select * from Produtos where id = {cod}'
        self.meu_cursor.execute(comando_sql)
        lista = self.meu_cursor.fetchall()
        for i in lista:
            print(i)

    def alterar_dados(self, atributo, valor, cod):
        comando_sql = f'update Produtos set {atributo} = "{valor}" where id = {cod}'
        self.meu_cursor.execute(comando_sql)
        self.conexao.commit()

    def excluir_produto(self, cod):
        comando_sql = f'delete from Produtos where id = {cod}'
        self.meu_cursor.execute(comando_sql)
        self.conexao.commit()
