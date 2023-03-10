from app.registros import Cliente, Venda, Produto
from datetime import datetime


def test_venda_nome_retorna_venda():
    c = Cliente("Luiz", "nick@email.com")
    p = Produto("Anel", 99.99, "dourado")
    d = datetime.today()
    v = Venda(p, c, d, 0)
    assert v.cliente == c and v.produto == p and v.data == d and v.parcelas == 0
