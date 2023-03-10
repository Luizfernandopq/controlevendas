from app.registros import Cliente


def test_cliente_nome_retorna_cliente():
    c = Cliente("Luiz", "nick@email.com")
    assert c.nome == "Luiz" and c.contato == "nick@email.com"
