import random

choices = ["سنگ", "کاغذ", "قیچی"]

while True:
    user = input("سنگ، کاغذ یا قیچی را انتخاب کنید (برای خروج exit): ")

    if user == "exit":
        print("بازی تمام شد.")
        break

    if user not in choices:
        print("انتخاب نامعتبر است.")
        continue

    computer = random.choice(choices)

    print("انتخاب کامپیوتر:", computer)

    if user == computer:
        print("مساوی شدید!")
    elif (user == "سنگ" and computer == "قیچی") or \
         (user == "کاغذ" and computer == "سنگ") or \
         (user == "قیچی" and computer == "کاغذ"):
        print("شما برنده شدید!")
    else:
        print("کامپیوتر برنده شد!")