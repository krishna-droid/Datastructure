from exo15 import out_of_stock_products

def test_out_of_stock_products():
    # Test case with out-of-stock products
    database_1 = {1: {"price": 20, "quantity": 0}, 2: {"price": 15, "quantity": 0}, 3: {"price": 25, "quantity": 0}}
    result_1 = out_of_stock_products(database_1)
    assert result_1 == [(3, {"price": 25, "quantity": 0}), (1, {"price": 20, "quantity": 0}), (2, {"price": 15, "quantity": 0})]

    # Test case with no out-of-stock products
    database_2 = {4: {"price": 30, "quantity": 5}, 5: {"price": 18, "quantity": 3}, 6: {"price": 22, "quantity": 8}}
    result_2 = out_of_stock_products(database_2)
    assert result_2 == []

    # Test case with an empty database
    database_3 = {}
    result_3 = out_of_stock_products(database_3)
    assert result_3 == []
