#تابعی به نام analyze_text(text) بنویسید که موارد زیر را پیدا کند:

'''تعداد کلمات
تعداد حروف
تعداد اعداد
پرتکرارترین حرف
پرتکرارترین کلمه
طولانی‌ترین کلمه
کوتاه‌ترین کلمه
تعداد کلمات Palindrome
تعداد حروف بزرگ
تعداد حروف کوچک'''
def analyze_text(text):
    words = text.split()

    letters = 0
    digit = 0
    up = 0
    low = 0
    palindrome_words = 0

    most_common_letter = ""
    most_common_word = ""
    longest_word = ""
    shortest_word = words[0]
    max_count = 0

    # شمارش حروف، اعداد، حروف بزرگ و کوچک
    for i in text:
        if i.isalpha():
            letters = letters + 1

        if i.isupper():
            up = up + 1

        if i.islower():
            low = low + 1

        if i.isdigit():
            digit = digit + 1

    # بررسی کلمات
    for word in words:
        if word == word[::-1]:
            palindrome_words += 1

        if len(word) > len(longest_word):
            longest_word = word

        if len(word) < len(shortest_word):
            shortest_word = word

    # پرتکرارترین حرف
    max_letter_count = 0

    for char in text:
        if char.isalpha():
            count = text.count(char)

            if count > max_letter_count:
                max_letter_count = count
                most_common_letter = char

    # پرتکرارترین کلمه
    max_word_count = 0

    for word in words:
        count = words.count(word)

        if count > max_word_count:
            max_word_count = count
            most_common_word = word

    result = {
        "words": len(words),
        "letters": letters,
        "digits": digit,
        "most_common_letter": most_common_letter,
        "most_common_word": most_common_word,
        "longest_word": longest_word,
        "shortest_word": shortest_word,
        "palindrome_words": palindrome_words,
        "uppercase": up,
        "lowercase": low
    }

    return result
text = input("Enter your text: ")
result = analyze_text(text)
print(result)