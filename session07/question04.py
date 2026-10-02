#تشخیص تراکنش‌های مشکوک
#تابعی به نام detect_fraud(transactions) بنویسید.
#تراکنش‌ها:

transactions = [
    ("Ali", "deposit", 50000000, 10),
    ("Ali", "withdraw", 2000000, 11),
    ("Ali", "withdraw", 3000000, 12),
    ("Ali", "withdraw", 4000000, 13),
    ("Ali", "withdraw", 5000000, 14),
    ("Ali", "withdraw", 6000000, 15),
    ("Sara", "deposit", 50000000, 20),
    ("Sara", "withdraw", 60000000, 21),
    ("Reza", "deposit", 150000000, 30)
]
#ساختار هر تراکنش:
#(username, type, amount, time)
#یک تراکنش مشکوک است اگر:
'''مبلغ بیشتر از 100 میلیون باشد.
بیش از ۳ برداشت پشت سر هم انجام شده باشد.
مبلغ برداشت بیشتر از موجودی باشد.
تابع باید تراکنش‌های مشکوک را برگرداند.'''
#چالش بسیار مهم:
#تابع detect_fraud() نباید خودش همه کارها را انجام دهد.
#آن را به چند تابع کوچک‌تر تقسیم کنید:

'''check_large_transaction()
check_repeated_withdrawals()
check_balance()
generate_fraud_report()'''
#در نهایت گزارشی از تراکنش‌ها را در تابع آخر برگردانید.



#هر تراکنش 4 بخش داره پس وقتی روی تراکنش حرکت کنیم:
for transaction in transactions:
#می‌توانیم آن را باز کنیم:
    username, transaction_type, amount, time = transaction

#اول ساده‌ترین تابع را می‌نویسیم.
#می‌خواهیم به تابع بگوییم مبلغ را بررسی کن.
def check_large_transaction(amount):
#اگر بیشتر از ۱۰۰ میلیون بود:
    if amount > 100000000:
        return True
#اگر نبود:
    return False


#تابع دوم: برداشت‌های پشت سر هم
#تابع باید بداند الان چند برداشت پشت سر هم داشته‌ایم.
#پس یک شمارنده می‌گیرد:
def check_repeated_withdrawals(withdraw_count):
#اگر بیشتر از ۳ باشد:
    if withdraw_count > 3:
        return True
    return False

#تابع سوم: بررسی موجودی
#آیا مبلغ برداشت از موجودی بیشتر است؟
#پس دو چیز لازم داریم:
def check_balance(balance, amount):
#اگر مبلغ بیشتر از موجودی بود:
    if amount > balance:
        return True
    return False

#تابع اصلی:

def detect_fraud(transactions):
# چند اطلاعات را نگه داریم:
#گزارش تراکنش‌های مشکوک
    fraud_transactions = []
#موجودی کاربران
    balances = {}
#تعداد برداشت‌های پشت سر هم
    withdraw_counts = {}
    for transaction in transactions:
        username, transaction_type, amount, time = transaction
        if username not in balances:
            balances[username] = 0
        if username not in withdraw_counts:
            withdraw_counts[username] = 0
        if transaction_type == "deposit":
            balances[username] += amount
            withdraw_counts[username] = 0
        elif transaction_type == "withdraw":
            withdraw_counts[username] += 1
            fraud_reasons = []
            if check_large_transaction(amount):
                fraud_reasons.append("Large transaction")
            if check_repeated_withdrawals(withdraw_counts[username]):
                fraud_reasons.append("Repeated withdrawals")
            if check_balance(balances[username], amount):
                fraud_reasons.append("Insufficient balance")
            if len(fraud_reasons) > 0:
                fraud_transactions.append({
                    "username": username,
                    "type": transaction_type,
                    "amount": amount,
                    "time": time,
                    "reasons": fraud_reasons
                })
            balances[username] -= amount
    return fraud_transactions
def generate_fraud_report(fraud_transactions):

    report = []

    for transaction in fraud_transactions:

        report.append(
            f"{transaction['username']} | "
            f"{transaction['type']} | "
            f"{transaction['amount']:,} | "
            f"Time: {transaction['time']} | "
            f"Reason: {', '.join(transaction['reasons'])}"
        )

    return report


fraud_transactions = detect_fraud(transactions)

report = generate_fraud_report(fraud_transactions)

for item in report:
    print(item)