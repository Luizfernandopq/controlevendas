from app.registros import Produto, Cliente
from datetime import datetime


class Venda:
    def __init__(self, produto: Produto, cliente: Cliente, data: datetime, parcelas: int = 0):
        self.produto = produto
        self.cliente = cliente
        self.data = data
        self.parcelas = parcelas