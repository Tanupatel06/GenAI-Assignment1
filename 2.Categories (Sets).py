products = {"notebook", "pen", "pencil", "eraser", "marker", "wireless mouse"}
categories_set = {"stationery", "electronics"}
print(categories_set)
categories_set.add("accessories")
print("After adding accessories:", categories_set)
categories_set.add("stationery")  # This will not add a duplicate
print("After trying to add stationery again:", categories_set)
print("Is stationery in categories?", "stationery" in categories_set)
print("total unique categories:", len(categories_set))