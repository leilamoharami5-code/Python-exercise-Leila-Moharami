## تحلیل تراکنش‌های مالی
'''داده‌های زیر را در نظر بگیرید:'''
transactions = [
    ("Ali", "deposit", 5000000),
    ("Ali", "withdraw", 1000000),
    ("Sara", "deposit", 8000000),
    ("Ali", "withdraw", 500000),
    ("Sara", "withdraw", 2000000),
    ("Reza", "deposit", 10000000)
]
'''تابع زیر را بنویسید:
analyze_transactions(transactions)
باید برای هر کاربر مشخص کند:
- Total Deposits
- Total Withdrawals
- Balance Change
- Number of Transactions
**به عنوان مثال:**
{
    "Ali": {
        "deposits": 5000000,
        "withdrawals": 1500000,
        "balance_change": 3500000,
        "transactions": 3
    }
}
سپس موارد زیر را حساب نمایید:
- بیشترین واریز
- بیشترین برداشت
- فعال‌ترین کاربر ...جواب این سوال بگو قدم به قدم انگار معلم هستی و قبل جواب توضیح ودلیلش بگو بعد جواب رو و ابنکه جوری کد بگم ک از کاربر ورودی بگیرم'''

def analyze_transactions(transactions):
    result = {}
#بررسی تراکنش ها
    for transaction in transactions:
        name, transaction_type, amount = transaction
        if name not in result:
            result[name] = {
                "deposits": 0,
                "withdrawals": 0,
                "balance_change": 0,
                "transactions": 0
            }
   #حالا که یک تراکنش برای یه اسم مثلا Ali پیدا کردیم، تعداد تراکنش‌هایش باید یکی شود.
        result[name]["transactions"] += 1
        #اگر واریز بود
        if transaction_type == "deposit":
            #باید مبلغ را به deposits اضافه کنیم
            result[name]["deposits"] += amount
            #و چون موجودی افزایش پیدا کرده:
            result[name]["balance_change"] += amount
#اگر برداشت بود
        elif transaction_type == "withdraw":
            #مبلغ رو به برداشت اضافه میکنم
            result[name]["withdrawals"] += amount
            #ولی موجودی باید کم بشه
            result[name]["balance_change"] -= amount
            #چون تابع تمام اطلاعات را محاسبه کرده و حالا باید نتیجه را برگرداند.
    return result
#پس بیرون تابع می‌توانیم بنویسیم:
result = analyze_transactions(transactions)
print(result)
result = analyze_transactions(transactions)

#برای بیشترین واریز, بیشترین برداشت, فعال ترین کاربر

#اول یک مقدار اولیه لازم داریم
max_deposit = 0
max_deposit_user = ""

max_withdrawal = 0
max_withdrawal_user = ""

max_transactions = 0
active_user = ""


for name, data in result.items():

    if data["deposits"] > max_deposit:
        max_deposit = data["deposits"]
        max_deposit_user = name

    if data["withdrawals"] > max_withdrawal:
        max_withdrawal = data["withdrawals"]
        max_withdrawal_user = name

    if data["transactions"] > max_transactions:
        max_transactions = data["transactions"]
        active_user = name


    print("\n--- Transaction Analysis ---")

for name, data in result.items():
    print(f"\nUser: {name}")
    print(f"  Total Deposits:    {data['deposits']:,}")
    print(f"  Total Withdrawals: {data['withdrawals']:,}")
    print(f"  Balance Change:    {data['balance_change']:,}")
    print(f"  Transactions:      {data['transactions']}")

print("\n--- Summary ---")
print(f"Highest Deposit:    {max_deposit_user} ({max_deposit:,})")
print(f"Highest Withdrawal: {max_withdrawal_user} ({max_withdrawal:,})")
print(f"Most Active User:   {active_user} ({max_transactions} transactions)")
















