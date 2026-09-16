employees = {
    "E01": {"name": "Ali", "age": 28, "salary": 3000},
    "E02": {"name": "Sara", "age": 32, "salary": 4500},
    "E03": {"name": "Reza", "age": 25, "salary": 2800}
}

max_salary = 0
min_salary = 999999
max_name = ""
min_name = ""
total = 0

for i in employees:
    salary = employees[i]["salary"]
    total += salary

    if salary > max_salary:
        max_salary = salary
        max_name = employees[i]["name"]

    if salary < min_salary:
        min_salary = salary
        min_name = employees[i]["name"]

    if salary > 3000:
        print("Bishtar az 3000:", employees[i]["name"])

print("Bishtarin hoghoogh:", max_name, max_salary)
print("Miyangin:", total / len(employees))
print("Kamtarin hoghoogh:", min_name, min_salary)