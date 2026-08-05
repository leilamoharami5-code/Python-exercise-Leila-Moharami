#تشخیص بازه زمانی روز
#عدد بین 10 تا 23 و مشخص بشه )صبح.ظهر.عصر.شب(
#اگر غیر بازه زمانی بود یه پیام نمایش بده
hours = int(input("please enter hours:"))
if 0 < hours < 6:
    print("mid night")
elif 7 < hours < 12:
    print("morning")
elif 13 < hours < 19 :
    print("noon/after noon")
elif 20 < hours < 23:
    print("night")
else:
    print("your day is over!")