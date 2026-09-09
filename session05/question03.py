#برنامه‌ای بنویسید که رشته ای از کاربر دریافت کرده و تعداد موارد زیر را محاسبه نماید:
#حروف انگلیسی
#حروف بزرگ
#حروف کوچک
#اعداد
#فاصله‌ها
#کاراکترهای خاص

#algoritm:
#6 variabe ba meghdar = 0
english = 0
up = 0
low = 0
num = 0
spaces = 0
countch = 0
ch = "@#$%&*_-?/!."
#daryaft input
print("*Your text must contain English letters, uppercase and lowercase letters*")
print("*and numbers,special characters, and spaces between letters*")
name = input("Please Enter Your Text: ")
#process -> peyda kardan mavared k mikham
#pas miam dakhel name harekat mikonam
for i in name:
#va baraye har kodom shart mizaram -> meghdar ghabl + 1
    if i.isalpha():
        english += 1
    if i.isupper():
        up += 1 
    if i.islower():
        low += 1
    if i.isdigit():
        num += 1
    if i.isspace():
        spaces += 1
    if i in ch:
        countch += 1
print(f"/letters: {english} /upper: {up} /lower: {low} /number: {num} /space: {spaces} /charactor: {countch}")

        
        