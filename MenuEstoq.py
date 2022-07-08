from DBestoque import DBestoq

class Menu:
    def __init__(self):
        estoque = DBestoq()


        while True:
            entrada = input('Informe a opção desejada'
                            '\n1 - Cadastrar produto'
                            '\n2 - Cadastrar Fabricante'
                            '\n3 - Listar um produto'
                            '\n4 - Editar descrição do produto'
                            '\n5 - Editar fabricante do produto'
                            '\n6 - Compra de produtos'
                            '\n7 - Venda de produtos'
                            '\n8 - Sair\n')

            if entrada == '1':
                cod = None
                descricao = input('Descrição do produto: ')
                id_fabricante = input('Id do fabricante: ')
                quantidade = input('Quantidade do produto: ')

                estoque.cadastrar_produto(cod, descricao, id_fabricante, quantidade)

            elif entrada == '2':
                cod = None
                nome = input('Nome do fabricante: ')

                estoque.cadastrar_fabricante(cod, nome)

            elif entrada == '3':
                cod = input('test:')
                estoque.listar_produto(cod)

            elif entrada == '4':
                cod = int(input('Informe o codigo do produto: '))
                valor = input('Nova descrição: ')
                atributo = 'descricao'

                estoque.alterar_dados(atributo, valor, cod)

            elif entrada == '5':
                cod = int(input('Informe o codigo do produto: '))
                valor = input("Codigo do fabricante: ")
                atributo = 'id_fabricante'

                estoque.alterar_dados(atributo, valor, cod)

            elif entrada == '6':

                pass
            elif entrada =='7':

                pass
            elif entrada == '8':
                break
            else:
                pass

menu = Menu()