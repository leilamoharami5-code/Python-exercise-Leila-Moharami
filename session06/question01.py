products = {
    "laptop": 1200,
    "phone": 800,
    "tablet": 500,
    "headphone": 150,
    "mouse": 50
}

# Geran tarin mahsoul
max_price = max(products.values())
for product, price in products.items():
    if price == max_price:
        print("Geran tarin mahsoul:", product, price)

# Arzan tarin mahsoul
min_price = min(products.values())
for product, price in products.items():
    if price == min_price:
        print("Arzan tarin mahsoul:", product, price)

# Miyangin gheymat
total = sum(products.values())
average = total / len(products)
print("Miyangin gheymat:", average)

# Mahsoulati ke gheymateshan bishtar az 500 ast
print("Mahsoulati ba gheymat bishtar az 500:")
for product, price in products.items():
    if price > 500:
        print(product, price)

# Majmoe gheymat tamam mahsoulat
print("Majmoe gheymat:", total)