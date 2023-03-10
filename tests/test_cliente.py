from app.registros import Cliente


def test_cliente_construtor():
    c = Cliente("Luiz", "nick@email.com")
    assert c.nome == "Luiz" and c.contato == "nick@email.com"
