'''تحلیل لاگ‌های سیستم
فایل logs.txt را به صورت زیر داریم:
توابع زیر را بنویسید:
count_successful_logins()
count_failed_logins()
find_suspicious_users()
generate_report()
قانون:
اگر کاربری حداقل 3 بار خطای 403 داشته باشد، مشکوک محسوب شود.
گزارش نهایی باید شامل
تعداد Login موفق
تعداد Login ناموفق
کاربران مشکوک
تعداد عملیات هر کاربر'''

#قدم ۱ — خواندن فایل
#اول باید اطلاعات فایل را وارد برنامه کنیم.
with open("logs.txt", 'r')as file:
    logs = file.readlines()
    #تمام خط‌ها را می‌خواند و داخل یک لیست قرار می‌دهد
#شمارش log های موفق

def count_successful_logins(logs):
    count = 0 
    for line in logs:

        if not line.strip():
            continue

        user, operation, status = line.strip().split(",")

        if operation == "LOGIN" and status == "200":
            count += 1

    return count

#شمارش log های ناموفق
def count_failed_logins(logs):
    count = 0
    for line in logs:
        if not line.strip():
            continue
        user, operation, status = line.strip().split(",")
        if operation == "LOGING" and status != "200":
            count += 1
    return count

#پیدا کردن کاربران مشکوک
def find_suspicious_users(logs):
    failed_403 = {}
    suspicious_users = []
    for line in logs:
        if not line.strip():
            continue
        user, operation, status = line.strip().split(",")
        if status == "403":
            failed_403 [user] = failed_403.get(user, 0)+1
            
    for user, count in failed_403.items():
        if count >= 3:
            suspicious_users.append(user)
    return suspicious_users

# ساخت گزارش نهایی:
def generate_report(logs):

    successful = count_successful_logins(logs)
    failed = count_failed_logins(logs)
    suspicious = find_suspicious_users(logs)

    operations = {}

    for line in logs:

        if not line.strip():
            continue

        user, operation, status = line.strip().split(",")

        operations[user] = operations.get(user, 0) + 1

    print("\n--- System Report ---")

    print("Successful Logins:", successful)

    print("Failed Logins:", failed)

    print("Suspicious Users:", suspicious)

    print("Operations Per User:")

    for user, count in operations.items():
        print(user, ":", count)

# اجرای گزارش
generate_report(logs)
    