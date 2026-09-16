products = {
    "P01": ("Laptop", 1200, 5),
    "P02": ("Phone", 800, 0),
    "P03": ("Tablet", 500, 12),
    "P04": ("Mouse", 50, 25),
    "P05": ("Keyboard", 100, 0)
}

max_arzesh = 0
max_mahsool = ""
kol_arzesh = 0

for code in products:
    name, gheymat, mojoodi = products[code]

    arzesh = gheymat * mojoodi

    if mojoodi > 0:
        print("Mojood:", name)
    else:
        print("Namojood:", name)

    print("Arzesh mojoodi:", arzesh)

    if arzesh > max_arzesh:
        max_arzesh = arzesh
        max_mahsool = name

    kol_arzesh += arzesh

print()
print("Mahsool ba bishtarin arzesh:", max_mahsool)
print("Bishtarin arzesh mojoodi:", max_arzesh)
print("Arzesh kol anbar:", kol_arzesh)