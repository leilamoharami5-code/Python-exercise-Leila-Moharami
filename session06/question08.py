users = [
    ("Ali", 25, "Python"),
    ("Sara", 30, "Java"),
    ("Reza", 22, "Python"),
    ("Mina", 28, "C++"),
    ("John", 35, "Python"),
    ("David", 30, "Java")
]

group = {}

# goroh bandi bar asas zaban
for name, age, language in users:

    if language in group:
        group[language].append((name, age))
    else:
        group[language] = [(name, age)]


print("Groups:")
for language in group:
    print(language, ":", group[language])


# miyangin sen har zaban
print("\nAverage age:")

for language in group:
    total_age = 0

    for name, age in group[language]:
        total_age += age

    average = total_age / len(group[language])

    print(language, ":", average)


# mosentarin karbar har zaban
print("\nOldest user:")

for language in group:
    old_name = ""
    old_age = 0

    for name, age in group[language]:
        if age > old_age:
            old_age = age
            old_name = name

    print(language, ":", old_name, old_age)


# zaban ba bishtarin karbar
best_language = ""
max_users = 0

for language in group:
    if len(group[language]) > max_users:
        max_users = len(group[language])
        best_language = language

print("\nLanguage with most users:", best_language)


# tamam zaban ha
print("\nAll languages:")

for language in group:
    print(language)