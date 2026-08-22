#حدس عدد تصادفی

import random

number = random.randint(1, 100)

while True:
    guess = int(input("یک عدد بین 1 تا 100 حدس بزنید: "))

    if guess < number:
        print("عدد را بزرگتر کن")
    elif guess > number:
        print("عدد کوچک‌تر کن")
    else:
        print("تبریک! حدس شما درست است.")
        break