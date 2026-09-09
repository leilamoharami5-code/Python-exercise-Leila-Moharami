#برنامه‌ای بنویسید که یک متن از کاربر دریافت کرده و گزارش زیر را تولید کند
#Total characters -> کل کارکترها
#Total words -> کلمات
#Total letters-> حروف
#Total digits->اعداد
#Total spaces->فاصله
#Total uppercase->حروف بزرگ
#Total lowercase->حروف کوچیک
#Longest word->بلند ترین کلمه
#Shortest word->کوتاه ترین کلمه
#Most repeated character->بیشترین کارکتر تکراری
#Most repeated word -> بیشترین کلمه تکراری
#start
#tarif chandin variable
ch = "@#!$%&*_-.?"
countch = 0
W = 0
L = 0 
NUM = 0 
SP = 0
UP = 0 
LOW = 0 
LWORD = ""
REWORD = ""
RECH = ""
max_count = 0
max_ch_count = 0
#get input:
text = input("Enter a text: ")
#text → کل متن، برای شمردن کاراکترها، حروف، اعداد، فاصله‌ها، بزرگ و کوچک
words = text.split()
#words → لیست کلمات، برای تعداد کلمات، بلندترین، کوتاه‌ترین و پرتکرارترین کلمه
SHWORD = words[0]
#words[0]-> چون لیست است و این یعنی اولین کلمه رو بگیر
#words[0][0] -> و دوباره در لیست این یعنی اولین حرف از اولین کلمه

#peymayesh ba for # بررسی کاراکترها
W = len(words)
for i in text:
    if i.isdigit():
        NUM += 1
    if i.isupper():
        UP += 1
    if i.islower():
        LOW += 1
    if i.isalpha():
        L += 1
    if i in ch:
        countch += 1
    if i == " ":
        SP += 1
        
#حلقه تمام.
#new for -> برای کلمات
for g in words:
    if len(g) > len(LWORD):
        LWORD = g
    if len(g) < len(SHWORD):
        SHWORD = g
    if words.count(g) > max_count:
        max_count = words.count(g)
        REWORD = g
for c in ch:
    count = text.count(c)
    if count > max_ch_count:
        max_ch_count = count
        RECH = c
    #end
print("Total characters:", len(text))
print("Total words:", W)
print("Total letters:", L)
print("Total digits:", NUM)
print("Total spaces:", SP)
print("Total uppercase:", UP)
print("Total lowercase:", LOW)
print("Longest word:", LWORD)
print("Shortest word:", SHWORD)
print("Most repeated character:", RECH)
print("Most repeated word:", REWORD)   
        