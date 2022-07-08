from Produtos import *

class estoq:
    def __init__(self):
        self.listaprodutos = []


    def cadastrar_produtos(self, cod, descricao, fabricante, quantidade):

        self.listaprodutos.append(Prod(cod,descricao,fabricante,quantidade))
        print('Cadastro realizado!')

    def listar_todos_produtos(self):
        for i in range(len(self.listaprodutos)):
            print('\n-codigo: ',self.listaprodutos[i].cod,
                  '\n-Descrição: ',self.listaprodutos[i].descricao,
                  '\n-Fabricante: ',self.listaprodutos[i].fabricante,
                  '\n-Quantidade: ',self.listaprodutos[i].quantidade,'\n')

    def listar_um_produto(self):
        cont = 0
        entrada = input('Informe o codigo do produto: ')
        for i in range(len(self.listaprodutos)):
            if entrada == self.listaprodutos[i].cod:
                print('\n-codigo: ', self.listaprodutos[i].cod,
                      '\n-Descrição: ', self.listaprodutos[i].descricao,
                      '\n-Fabricante: ', self.listaprodutos[i].fabricante,
                      '\n-Quantidade: ', self.listaprodutos[i].quantidade,'\n')
            else:
                cont += 1
                if cont == len(self.listaprodutos):
                    for i in range(len(self.listaprodutos)):
                        print('\n-codigo: ', self.listaprodutos[i].cod,
                              '\n-Descrição: ', self.listaprodutos[i].descricao,
                              '\n-Fabricante: ', self.listaprodutos[i].fabricante,
                              '\n-Quantidade: ', self.listaprodutos[i].quantidade, '\n')

    def alterar_descricao(self):
        cont = 0
        entrada = input('Informe o codigo do produto: ')
        for i in range(len(self.listaprodutos)):
            if entrada == self.listaprodutos[i].cod:
                self.listaprodutos[i].descricao = input('Nova descrição:')
        else:
            cont += 1
            if cont == len(self.listaprodutos):
                print('Codigo nao encontrado')

    def alterar_fabricante(self):
        cont = 0
        entrada = input('Informe o codigo do produto: ')
        for i in range(len(self.listaprodutos)):
            if entrada == self.listaprodutos[i].cod:
                self.listaprodutos[i].fabricante = input('Novo fabricante:')
        else:
            cont += 1
            if cont == len(self.listaprodutos):
                print('Codigo nao encontrado')
