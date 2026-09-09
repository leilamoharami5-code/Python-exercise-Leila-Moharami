#برنامه‌ای بنویسید که یک جمله دریافت کند و طولانی‌ترین کلمه را پیدا نماید
#اگر چند کلمه طول یکسان داشتند، 
#اولین کلمه نمایش داده شود.
#Algoritm:
#yek vaiable -> braye meghdar
more = 0
#yek variable-> baraye kalame
words = ""

#get sentence 
a = input("enter your favorite sentence: ")
#joda kardan kalamat -> tabdil be reshte
r = a.split(" ")
#process-> baresi len kalamat
for i in r:
    lenc = len(i)
    if lenc > more:
        more = lenc
        words = i
print(f"word: {words} {more}")
        
#end
 