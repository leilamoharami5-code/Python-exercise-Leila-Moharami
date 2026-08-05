route = int(input('enter your kilometer : '))
pay = 20000
more = ((route-2)*5000) + pay
if route < 2:
    print(pay)
else:
    print(more)