#از کاربر 10 عدد بگیر  و میانگین انرا حساب کن
#الگوریتم:
#ورودی: از کاربر 10 عدد بگیر
#عملیات: جمع اعداد و تقسیم بر 10 یا تعداد اعداد
#چاپ خروجی

#ultra qestion
#kare tekrari darim ya na? yes
#kare tekrari chie? gereftan 10 adad , mohasebe on
#tekrar moshakhase ya na? yes
#for or while? for
a = 0
for i in range(10):
    adad = int(input(" عدد خود را وارد کنید: "))
#b = a + adad
#خط بالا ارور داد چونکه a رو هر بار 0 در نظر میگیره و انگار 0 با عدد جدید جمع میکنه
    a = a + adad
result = a / 10
print(f"result : {result}")