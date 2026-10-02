'''تحلیل لاگ‌های سیستم
داده‌ها به صورت زیر داریم:'''

logs = [
    ("Ali", "LOGIN", 200),
    ("Ali", "DOWNLOAD", 200),
    ("Sara", "LOGIN", 403),
    ("Reza", "LOGIN", 200),
    ("Sara", "LOGIN", 403),
    ("Sara", "LOGIN", 403),
]
'''سیستمی بسازید که:

تعداد Login موفق را پیدا کند.
تعداد Login ناموفق را پیدا کند.
اگر یک کاربر حداقل ۳ خطای 403 داشت، او را مشکوک اعلام کند.
تعداد عملیات هر کاربر را محاسبه کند.
گزارش نهایی تولید کند.'''
#متغیرهای اولیه را بسازیم
#اول تعداد Loginهای موفق و ناموفق را صفر می‌گذاریم:

successful_logins = 0
failed_logins = 0
#برای تعداد عملیات هر کاربر یک دیکشنری می‌خواهیم:
operations = {}
#و برای تعداد خطاهای 403 هر کاربر هم یک دیکشنری:
failed_403 = {}
for log in logs:
    username, operation, status_code = log
    #اول باید ببینیم کاربر قبلاً در دیکشنری هست یا نه:

    if username not in operations: 
        operations[username] = 0
    
#بعد یکی به تعداد عملیاتش اضافه کنیم:
    operations[username] += 1
#یعنی هر وقت هم Login بود و هم کد 200 داشت، یکی به Login موفق اضافه کن.
    if operation == "LOGIN" and status_code == 200:
        successful_logins += 1

#حالا اگر Login باشد و کد 403 باشد:

    elif operation == "LOGIN" and status_code == 403:
        failed_logins += 1
#باید تعداد خطاهای 403 برای هر کاربر جداگانه ذخیره شود.
    if username not in failed_403:
        failed_403[username] = 0
        #برای افزایش دادن باید بیرون if باشد.
    failed_403[username] += 1

#حالا یک لیست برای کاربران مشکوک می‌سازیم:
print("failed_403 =", failed_403)
suspicious_users = []

#بعد روی دیکشنری حرکت می‌کنیم:

for username, count in failed_403.items():
    if count >= 3:
        suspicious_users.append(username)
print("\n--- System Log Analysis ---")
'''چرا >= 3؟
چون سؤال گفته:
حداقل ۳ خطای 403
پس هم ۳ و هم بیشتر از ۳ باید مشکوک شوند.'''
print(f"Successful Logins: {successful_logins}")
print(f"Failed Logins: {failed_logins}")

print("\nOperations Per User:")

    
    
for username, count in operations.items():
    print(f"  {username}: {count} operations")
print("\nSuspicious Users:")

for username in suspicious_users:
    print(f"  {username}")
    









