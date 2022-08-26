from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        id=1,
        nome_do_produto="Dorflex",
        nome_da_empresa="Farmacon",
        data_de_fabricacao="2022-10-20",
        data_de_validade="2024-10-20",
        numero_de_serie="123456",
        instrucoes_de_armazenamento="em local seco"
    )

    assert product.id == 1
    assert product.nome_do_produto == "Dorflex"
    assert product.nome_da_empresa == "Farmacon"
    assert product.data_de_fabricacao == "2022-10-20"
    assert product.data_de_validade == "2024-10-20"
    assert product.numero_de_serie == "123456"
    assert product.instrucoes_de_armazenamento == "em local seco"
