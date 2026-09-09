#برنامه‌ای بنویسید و یک سیستم Login طراحی کنید
#که user و password را از کاربر دریافت کند
#کاربر حداکثر ۳ بار فرصت ورود داشته باشد.
#اگر نام کاربری یا رمز عبور اشتباه بود ﭘﯿﺎم زﯾﺮ
#ﺑﻪ ﻫﻤﺮاه ﺗﻌﺪاد ﺗﻼش ﻧﺎﻣﻮﻓﻖ نمایش داده شود.
#Wrong username or password
#Atempts remaining: 2
#اگر اطلاعات درست بود، پیام Login successful نمایش داده شود.

user = "leila.moharami"
passw = "@l_m1234"
attemts_counter = 0
while attemts_counter < 3:
    mainuser = input("enter your username: ")
    mainpass = input("enter your password: ")

    if mainuser == user and mainpass == passw:
        print("login succsesfuly :)")
        break
    else:
        attemts_counter = attemts_counter + 1
        y = 3 - attemts_counter
        print(f'Wrong username or password')
        print(f'remaining attempts --> {y}')


