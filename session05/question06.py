#برنامه ایی بنویسید که یک متن دریافت نمایید
#اگر متن شامل هرکدام از کلمات زیر بود:
#fraud_scam_password_atack
#آن کلمه را پیدا و تعداد مقدار آن را نمایش دهید.
#ALGORITM:
#variable ba meghdar tarif shode
num = 0
word = ""
text = ['fraud','hack','scam','password','attack']
#daryaft input:
t = input("Make a sentence using these words-> 'fraud scam hack password attack' : ")
x = t.split(" ")
for i in x:
    if i in text and i != word:
        print(i, x.count(i))
        word = i
        

        
    