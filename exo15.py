def out_of_stock_products(product_database):
    # Filter products with quantity in stock equal to 0
    out_of_stock = {product_id: product_info for product_id, product_info in product_database.items() if product_info["quantity"] == 0}

    # Sort out-of-stock products by price (descending) and then by product ID (ascending)
    sorted_out_of_stock = sorted(out_of_stock.items(), key=lambda x: (x[1]["price"], x[0]), reverse=True)

    return sorted_out_of_stock

# Uncomment the line below to test the function
# out_of_stock_products({1: {"price": 20, "quantity": 0}, 2: {"price": 15, "quantity": 0}, 3: {"price": 25, "quantity": 0}})
