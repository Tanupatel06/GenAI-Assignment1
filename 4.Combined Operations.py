products = ["notebook","pen","pencil","eraser","marker","wireless mouse"]
price_dict = {"notebook": 60, "pen": 5, "pencil": 2, "eraser": 1.5, "marker": 3, "wireless mouse": 25.75}
catalog = ("procuct_name: notebook , price: $60 , category: stationery\n"
           "procuct_name: pen , price: $5 , category: stationery,\n"
           "procuct_name: pencil , price: $2 , category: stationery,\n"
           "procuct_name: eraser , price: $1.5 , category: stationery,\n"
           "procuct_name: marker , price: $3 , category: stationery,\n"
           "procuct_name: wireless mouse , price: $25.75 , category: electronics")
print("Product Catalog:\n", catalog)
category_to_products = {}
for product in products:
    if product in catalog:
        category = "stationery" if product != "wireless mouse" else "electronics"
        if category not in category_to_products:
            category_to_products[category] = []
        category_to_products[category].append(product)
print("Category to Products Mapping:", category_to_products)
