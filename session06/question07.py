orders = [
    ("Ali", "Laptop"),
    ("Sara", "Phone"),
    ("Ali", "Phone"),
    ("Reza", "Laptop"),
    ("Sara", "Laptop"),
    ("Ali", "Tablet"),
    ("Reza", "Phone")
]

customers = {}

for customer, product in orders:

    if customer in customers:
        customers[customer].append(product)
    else:
        customers[customer] = [product]

print(customers)