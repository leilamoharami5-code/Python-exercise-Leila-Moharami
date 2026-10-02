## مدیریت کاربران با فایل
'''فایلی به نام **users.txt** داریم که هر خط آن به شکل زیر است:
```
Ali,12345,active
Sara,abc789,active
Reza,45678,blocked
``
توابع زیر را بنویسید:
- **add_user()**
- **find_user()**
- **delete_user()**
- **generate_report()**
**قوانین:**
- تابع **add_user()** کاربر جدید را به فایل اضافه کند.
- اگر username قبلاً وجود داشت، کاربر اضافه نشود.
- تابع **find_user()** بر اساس username کاربر را پیدا کند.
- تابع **delete_user()** کاربر را حذف کند.
- تابع **generate_report()** تعداد کاربران فعال و مسدود را نمایش دهد.'''

'''r = Read = بخون 📖
w = Write = از نو بنویس ✍️
a = Append = به آخرش اضافه کن ➕'''

#پیدا کردن کاربر
def find_user(username):
    with open("users.txt", "r") as file:
       # with هم باعث می‌شود بعد از تمام شدن کار، فایل به‌درستی بسته شود
        for line in file:
            line = line.strip() #فاصله رو حذف میکنه

            user, password, status = line.split(",") #جدا کردن اطلاعات با کاما

            if user == username:
                return {
                    "username": user,
                    "password": password,
                    "status": status
                }
    return None
#اضافه کردن کاربر
def add_user(username,password,status):
    file = open('users.txt','r')
    for line in file:
        data = line.strip().split(',')
        if data[0] == username:
            print('username allready exests!')
            file.close()
            return
    file.close()
    file = open("users.txt", "a")  #یعنی به انتهای فایل اضافه کن و اطلاعات قبلی را پاک نکن.
    file.write(f"{username},{password},{status}\n")
    #این n\ یعنی برو خط بعد؛ وگرنه کاربر بعدی ممکن است به انتهای همین خط بچسبد
        
    file.close()
print("User added successfully!")
#مثلاً اگر صدا بزنیم:
add_user("Mina", "78945", "active")
#این خط به فایل اضافه می‌شود:
#Mina,78945,active

# حذف کاربر
def delete_user(username):
    file = open("users.txt", "r")
    lines = file.readlines()
    file.close()
    found = False
    new_lines = []
    # همه خطوط را بررسی می‌کنیم
    for line in lines:
        data = line.strip().split(",")
        if data[0] == username:
            found = True
        else:
            new_lines.append(line)
    file = open("users.txt", "w")

    for line in new_lines:
        file.write(line)

    file.close()

    if found:
        print("User deleted successfully!")
    else:
        print("User not found!")
        # ساخت گزارش
def generate_report():

    active_users = 0
    blocked_users = 0

    file = open("users.txt", "r")

    for line in file:

        data = line.strip().split(",")

        status = data[2]

        if status == "active":
            active_users += 1

        elif status == "blocked":
            blocked_users += 1

    file.close()

    print("\n--- User Report ---")
    print(f"Active Users: {active_users}")
    print(f"Blocked Users: {blocked_users}")
    
generate_report()

    
    