#برنامه‌ای بنویسید که دو جمله از کاربر دریافت کرده و مشخص کند چه کلماتی در هر دو جمله وجود دارند

commen_word = ""
text1 = input("یک جمله وارد کنید :")
text2 = input("یک جمله وارد کنید :")
a = text1.split()
b = text2.split()

for i in a: 
    for g in b:
        if i == g:
           commen_word += i + ", "
print(f"commen word : {commen_word}")