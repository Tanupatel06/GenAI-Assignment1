price_dict = {"notebook": 60, "pen": 5, "pencil": 2, "eraser": 1.5, "marker": 3, "wireless mouse": 25.75}
print(price_dict)
price_dict["Smart Watch"] = 150
print(price_dict)
price_dict["notebook"] = 65
print(price_dict)
if("pencil" in price_dict):
    del price_dict["pencil"]
else:
    print("pencil not found in price_dict")
print(price_dict)
Average_price = sum(price_dict.values()) / len(price_dict)
print("Average price of products:", Average_price)