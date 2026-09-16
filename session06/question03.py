text = input("Enter a sentence: ")

letters = {}

# roye har character hareket mikonim
for i in text:

    # faghat horof ro dar nazar migirim
    if i.isalpha():

        # agar harf ghablan vojood dasht
        if i in letters:
            letters[i] += 1

        # agar harf baraye avalin bar didim
        else:
            letters[i] = 1

print(letters)