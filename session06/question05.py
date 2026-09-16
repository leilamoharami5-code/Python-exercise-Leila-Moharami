students = {
    "Ali": [18, 17, 20],
    "Sara": [15, 19, 18],
    "Reza": [12, 14, 10],
    "Mina": [20, 20, 19]
}

best_name = ""
best_average = 0

for name in students:
    nomreha = students[name]

    average = sum(nomreha) / len(nomreha)
    max_nomre = max(nomreha)

    if average >= 15:
        status = "Passed"
    else:
        status = "Failed"

    print(name)
    print("Average:", round(average, 2))
    print("Status:", status)
    print("Max score:", max_nomre)
    print()

    if average > best_average:
        best_average = average
        best_name = name

print("Best student:", best_name)
print("Highest average:", round(best_average, 2))