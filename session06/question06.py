sales = (
    ("Ali", "Laptop", 1200),
    ("Sara", "Phone", 800),
    ("Ali", "Phone", 800),
    ("Reza", "Laptop", 1200),
    ("Sara", "Laptop", 1200),
    ("Ali", "Mouse", 50)
)

customers = {}
products = {}
total = 0

for customer, product, price in sales:

    # hesab kharid har moshtari
    if customer in customers:
        customers[customer] += price
    else:
        customers[customer] = price

    # tedad forosh har mahsool
    if product in products:
        products[product] += 1
    else:
        products[product] = 1

    # majmoe daramad
    total += price


# namayesh kharid moshtari ha
for customer in customers:
    print(customer, "→", customers[customer])

# moshtari ba bishtarin kharid
best_customer = ""
best_buy = 0

for customer in customers:
    if customers[customer] > best_buy:
        best_buy = customers[customer]
        best_customer = customer

print("Best customer:", best_customer)

# tedad forosh mahsoolat
for product in products:
    print(product, "→", products[product])

print("Total sales:", total)