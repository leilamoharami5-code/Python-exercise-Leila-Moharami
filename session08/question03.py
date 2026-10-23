## تحلیل تراکنش‌های مالی
'''فایل **transactions.txt** را به صورت زیر داریم
توابع زیر را بنویسید:

- **calculate_balance()**
- **total_deposits()**
- **total_withdrawals()**
- **find_invalid_transactions()**
- **generate_report()**
**قوانین:**
اگر برداشت یک کاربر بیشتر از موجودی او باشد، تراکنش نامعتبر است.
گزارش باید برای هر کاربر شامل موارد زیر باشد:
- نام
- مجموع واریز
- مجموع برداشت
- موجودی
- تراکنش‌های نامعتبر این سوال کد بگو مرحله به مرحله با اموزش'''

def total_deposits(transactions, user):
    total = 0

    for name, transaction_type, amount in transactions:
        if name == user and transaction_type == "deposit":
            total += amount

    return total


def total_withdrawals(transactions, user):
    total = 0

    for name, transaction_type, amount in transactions:
        if name == user and transaction_type == "withdraw":
            total += amount

    return total


def calculate_balance(transactions, user):
    balance = 0

    for name, transaction_type, amount in transactions:
        if name != user:
            continue

        if transaction_type == "deposit":
            balance += amount

        elif transaction_type == "withdraw":
            if amount <= balance:
                balance -= amount

    return balance


def find_invalid_transactions(transactions, user):
    balance = 0
    invalid = []

    for name, transaction_type, amount in transactions:
        if name != user:
            continue

        if transaction_type == "deposit":
            balance += amount

        elif transaction_type == "withdraw":
            if amount > balance:
                invalid.append(
                    (name, transaction_type, amount)
                )
            else:
                balance -= amount

    return invalid


def generate_report(transactions):
    users = []

    for user, transaction_type, amount in transactions:
        if user not in users:
            users.append(user)

    for user in users:
        deposits = total_deposits(transactions, user)
        withdrawals = total_withdrawals(transactions, user)
        balance = calculate_balance(transactions, user)
        invalid = find_invalid_transactions(transactions, user)

        print("\nنام:", user)
        print("مجموع واریز:", deposits)
        print("مجموع برداشت:", withdrawals)
        print("موجودی:", balance)
        print("تراکنش‌های نامعتبر:")

        if invalid:
            for transaction in invalid:
                print(transaction)
        else:
            print("موردی وجود ندارد")


# خواندن فایل
transactions = []

with open("transactions.txt", "r") as file:
    for line in file:
        if not line.strip():
            continue

        user, transaction_type, amount = line.strip().split(",")
        amount = int(amount)

        transactions.append(
            (user, transaction_type, amount)
        )

# نمایش گزارش نهایی
generate_report(transactions)
