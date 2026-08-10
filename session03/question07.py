#3 rang az karbar begir
#agar 2 rang barabar bod ......
#agar 3 rang barabar bod....
#agar nabod .....
color = input(" نام رنگ 1 را وارد کن : ")
n1 = color
color = input(" نام رنگ 2 را وارد کن : ")
n2 = color
color = input(" نام رنگ 3 را وارد کن : ")
n3 = color
if n1 == n2 and n1 == n3:
    print("رنگ ها تکراری میباشد ")
elif n1 == n3:
    print("رنگ 1 و 3 تکراری میباشد ")
elif n2 == n3:
    print("رنگ 3 و 2 تکراری میباشد ")
elif n1 == n2:
    print("رنگ 1 و 2 تکراری میباشد ")
else:
    print("رنگ ها باهم به توافق نرسیدند\U0001F605")
