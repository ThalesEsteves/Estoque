class Prod:
    def __init__(self, cod, descricao, fabricante, quantidade):
        self.cod = cod
        self.descricao = descricao
        self.id_fabricante = fabricante
        self.quantidade = quantidade


class Fabri:
    def __init__(self, cod, nome):
        self.cod = cod
        self.nome = nome
