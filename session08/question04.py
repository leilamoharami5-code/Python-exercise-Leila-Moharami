def get_values():
    n = int(input("تعداد مقادیر: "))
    values = []

    for i in range(n):
        value = input("مقدار را وارد کنید: ")
        values.append(value)

    return values

def add_unique(value, unique_values):
    for i in range(len(unique_values)):
        if unique_values[i].lower() == value.lower():
            return False, i + 1

    unique_values.append(value)
    return True, len(unique_values)

def process_values(values):
    unique_values = []
    duplicate_count = 0
    first_positions = []
    results = []

    for value in values:
        if value == "":
            results.append("empty")
            continue

        is_new, position = add_unique(value, unique_values)

        if is_new:
            first_positions.append(len(unique_values))
            results.append(("new", value))
        else:
            duplicate_count += 1
            results.append(("duplicate", value, position))

    return unique_values, duplicate_count, first_positions, results
def show_report(unique_values, duplicate_count,
                first_positions, results):

    for result in results:
        if result == "empty":
            print("مقدار خالی است و اضافه نشد.")
        elif result[0] == "new":
            print("مقدار جدید اضافه شد:", result[1])
        else:
            print("مقدار تکراری:", result[1],
                  "اولین موقعیت:", result[2])

    print("\nمقادیر یکتا:", unique_values)
    print("تعداد مقادیر یکتا:", len(unique_values))
    print("تعداد مقادیر تکراری:", duplicate_count)
    print("موقعیت اولین ورود:")

    for i in range(len(unique_values)):
        print(unique_values[i], "→", first_positions[i])
        
values = get_values()

unique_values, duplicate_count, first_positions, results = process_values(values)

show_report(unique_values, duplicate_count, first_positions, results)