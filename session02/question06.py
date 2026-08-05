kala = int(input('enter number: '))
a = (kala*15)/100
b = (kala*10)/100
c = (kala)
if kala > 1000:
    print(a)
elif 500 <= kala < 1000 :
    print(b)
else:
    print(c)