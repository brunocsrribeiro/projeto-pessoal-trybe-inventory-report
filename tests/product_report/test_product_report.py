from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        id=1,
        nome_do_produto="Dorflex",
        nome_da_empresa="Farmacon",
        data_de_fabricacao="2022-10-20",
        data_de_validade="2024-10-20",
        numero_de_serie="123456",
        instrucoes_de_armazenamento="em local seco"
    )

    assert product.__repr__() == (
        f"O produto {product.nome_do_produto} "
        f"fabricado em {product.data_de_fabricacao} "
        f"por {product.nome_da_empresa} com validade "
        f"até {product.data_de_validade} "
        f"precisa ser armazenado {product.instrucoes_de_armazenamento}."
    )
