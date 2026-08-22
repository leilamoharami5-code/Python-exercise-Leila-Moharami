sum_numbers = 0

while True:
    number = int(input("یک عدد وارد کنید: "))

    if number == 0:
        break

    sum_numbers += number

print("جمع اعداد:", sum_numbers)