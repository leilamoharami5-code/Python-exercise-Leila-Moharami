text = input('enter your account number : ')
#a4 = text[-17: 0: -1] -> this was wrong
#result = int(a4) اشتباهی ک کردم و خطایی که دادپایینه
#ValueError: invalid literal for int() with base 10: ''
#چون داشتم یه شماره حساب برعکس را به int تبدیل میکردم ولی اون رشته بود
result = text[ : : -1]
#مفهوم خط بالا یعنی از اول رشته شروع کن تا اخر برو با گام 1- حرکت کن
print(result)