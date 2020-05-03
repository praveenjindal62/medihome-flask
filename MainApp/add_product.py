from models.Product import Product
product_dict=[
    {
        "name":"Betnesol",
        "price":23.45,
        "company":"Pfizer",
        "solution":"Hydrocloric Acid"
    },
    {
        "name":"Sporlac",
        "price":2.45,
        "company":"Pfizer",
        "solution":"Hydrocloric Acid"
    }
]

prodObj=Product()
prodObj.insert(product_dict)