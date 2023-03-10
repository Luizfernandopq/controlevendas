from app.registros import Venda


class Cliente:
    def __init__(self, nome: str, contato: str):
        self.nome = nome
        self.contato = contato
        self.compras = []
        self.produtos = []

    def add_compra(self, venda: Venda):
        self.compras.append(venda)
        self.produtos.append(venda.produto)
