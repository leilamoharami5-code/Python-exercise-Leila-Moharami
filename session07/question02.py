

#قدم ۱ — ساخت تابع# قدم ۱ — ساخت تابع
def process_order(customer, *products, **options):

    # قدم ۲ — فعلاً تابع را صدا بزن
    print(customer)
    print(products)
    print(options)

    # قدم ۳ — حالا خروجی موردنظر را بساز
    order = {
        "customer": customer,
        "products": list(products),
        "discount": options.get("discount", 0),
        "tax": options.get("tax", 0),
        "shipping": options.get("shipping", 0),
        "final_price": 0
    }
    return order

    
'''چرا این مقدارها؟
"customer": customer → اسم مشتری را از پارامتر می‌گیرد.
"products": list(products) → همه محصولاتی که با *products گرفته‌ای را به لیست تبدیل می‌کند.
"discount": options.get("discount", 0) → اگر تخفیف داده شد همان را می‌گیرد؛ اگر داده نشد 0.
"tax": options.get("tax", 0) → اگر مالیات داده شد همان را می‌گیرد؛ اگر داده نشد 0.
"shipping": options.get("shipping", 0) → هزینه ارسال را می‌گیرد؛ اگر داده نشد فعلاً 0.
"final_price": 0 → فعلاً موقتاً صفر گذاشتیم، چون هنوز فرمول قیمت نهایی و قیمت محصولات را نداریم.'''


result = process_order(
    "Ali",
    "Laptop",
    "Mouse",
    "Keyboard",
    discount=10,
    tax=9,
    shipping=200000
)

print(result)


